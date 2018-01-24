#!/usr/bin/python

import os

ANSIBLE_METADATA = {
    'metadata_version': '0.1',
    'status': ['preview'],
    'supported_by': 'tchia04@gmail.com'
}

DOCUMENTATION = '''
---
module: load_average

short_description: Display load average info on host

version_added: "2.4"

description:
    - "This module displays the load average information on the target host"

options:
  none

extends_documentation_fragment:

author:
    - Tony Chia (@tchia)
'''

EXAMPLES = '''
- name: Display the load average on the targeted host
  load_average:

'''

RETURN = '''
    description: load average value from the os.getloadavg()
    returned: success
    type: string
    sample: (2.0810546875, 2.08544921875, 2.36669921875)
'''

from ansible.module_utils.basic import AnsibleModule

def run_module():
    # define the available arguments/parameters that a user can pass to
    # the module
    module_args = dict(
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # change is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        message=''
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        return result

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)
#    result['original_message'] = module.params['name']
#    result['message'] = 'goodbye'
#    load_avg_string=uptime | cut -d, -f4 | cut -d: -f2
    load_avg_string=os.getloadavg()
    result['message'] = load_avg_string

    # use whatever logic you need to determine whether or not this module
    # made any modifications to your target
    #if module.params['new']:
    result['changed'] = False

    # during the execution of the module, if there is an exception or a
    # conditional state that effectively causes a failure, run
    # AnsibleModule.fail_json() to pass in the message and the result
    #if module.params['name'] == 'fail me':
    if load_avg_string:
      # in the event of a successful module execution, you will want to
      # simple AnsibleModule.exit_json(), passing the key/value results
       module.exit_json(**result)
    else:
        module.fail_json(msg='Unable to get load average', **result)

    #module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()

