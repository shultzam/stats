# stats
Simple statistics application that takes in JSON serialized data and keeps a running average of the time (duration) of an action.

## Dependancies
- Python3.
  - This was developed using Python 3.7.5 but I expect any recent (3.5+) Python3 should work fine.
- Standard Python3 library: 
  - <code>json</code>

## Execution
- execute: <pre><code>./stats.py</code></pre>
- This assumes that Python3 is setup in your PATH variable in the standard location (/usr/bin/). If not you can execute: <pre><code>/path/to/python3 stats.py</code></pre> while using the absolute path to your Python3 binary.
- Note that stats.py has no output.

## Testing
- execute: <pre><code>./tst_stats.py</code></pre>
- Similar to above, this assumes that Python3 is setup in your PATH variable in the standard location (/usr/bin/). If not you can execute: <pre><code>/path/to/python3 tst_stats.py</code></pre> while using the absolute path to your Python3 binary.

## Notes/Assumptions
- It was assumed that 'jump' and 'run' were not the only actions that could be given. As such actions are accepted by <code>addAction</code> without n verification of action name. Additionally, an action 'spin' was tested.
- There are some nasty one-liners in <code>tst_getStats</code> used to retrieve specific entries from the results of <code>getStats</code>. They are not the most readable to some, including me, but alternatives I am aware of (for-loop/if-conditional, map() + itemgetter(), etc.) were not much better in my opinion.
- Normally I would prefer src and test subdirectories for stat.py and tst_stat.py but having subdirectories for one file each felt silly so both files exist in the project root directory.
