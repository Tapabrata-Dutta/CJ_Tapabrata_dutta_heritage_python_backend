log_entries = ['INFO', 'DEBUG', 'WARNING', 'ERROR', 'INFO', 'CRITICAL']


print('Scanning security logs...')
for entry in log_entries:
    print(f'Checking: {entry}')
    if entry == 'ERROR':
        print('🚨 Critical issue found! Stopping scan.')
        break
print('Scan complete.')
