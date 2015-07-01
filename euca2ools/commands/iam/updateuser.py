# Copyright 2009-2015 Eucalyptus Systems, Inc.
#
# Redistribution and use of this software in source and binary forms,
# with or without modification, are permitted provided that the following
# conditions are met:
#
#   Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
#
#   Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from requestbuilder import Arg

from euca2ools.commands.iam import IAMRequest, AS_ACCOUNT, arg_user


class UpdateUser(IAMRequest):
    DESCRIPTION = 'Change the name and/or path of a user'
    ARGS = [arg_user(help='name of the user to update'),
            Arg('-n', '--new-user-name', dest='NewUserName', metavar='USER',
                help='new name for the user'),
            Arg('-p', '--new-path', dest='NewPath', metavar='PATH',
                help='new path for the user'),
            Arg('--enabled', dest='Enabled', choices=('true', 'false'),
                help='''[Eucalyptus only] 'true' to enable the user, or 'false'
                        to disable the user'''),
            Arg('--pwd-expires', dest='PasswordExpiration',
                metavar='YYYY-MM-DDThh:mm:ssZ', help='''[Eucalyptus only]
                New password expiration date, in ISO8601 format'''),
            Arg('--reg-status', dest='RegStatus',
                choices=('REGISTERED', 'APPROVED', 'CONFIRMED'),
                help='''[Eucalyptus < 4.2 only] new registration status. Only
                        CONFIRMED users may access the system.'''),
            AS_ACCOUNT]
