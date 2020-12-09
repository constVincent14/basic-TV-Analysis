import seaborn as sns 
import pandas as pd
import matplotlib.pyplot as plt
# reading filePath before importing!
pathOne = input('Filepath Halftime Musicians: ')
pathTwo = input('Filepath Super Bowls: ')
pathThree = input('Filepath tvShows: ')
# reading data!
dataMusicians = pd.read_csv(pathOne)
dataBowls = pd.read_csv(pathTwo)
dataShows = pd.read_csv(pathThree)
# examine the data head
print('Halftime Musicians', dataMusicians.head(), sep='\n')
print('Super Bowls', dataBowls.head(), sep='\n')
print('Household with TV', dataShows.head(), sep='\n')

# PLOTTING THE DISTRIBUTION: CHECKING
plt.style.use('seaborn')
plt.hist(dataBowls['combined_pts'], label='Combined Points', color='green')
plt.xlabel('Combined Points'); plt.title('Distribution of Combined Points')
plt.ylabel('Number of Super Bowls')
plt.legend()
plt.show()
# SEARCH FOR DATA WITH LOWEST COMBINED SCORES AND THE HIGHEST
max_points = dataBowls[dataBowls['combined_pts']>70]
min_points = dataBowls[dataBowls['combined_pts']<25]
print(max_points, min_points, sep='\n')
# Lihat distribusi perbedaan points: 'difference_pts'
plt.style.use('seaborn')
plt.hist(dataBowls['difference_pts'], label='Difference Points', color='purple')
plt.xlabel('Difference Points'); plt.ylabel('Number of Super Bowls'); plt.title('Distribution of Difference Points')
plt.legend(); plt.show()
# SEARCH FOR DATA WITH THE SMALLEST AND HIGHEST Difference Points
print(dataBowls[dataBowls['difference_pts']>36],
      dataBowls[dataBowls['difference_pts']<=2], sep='\n')
# coba lihat apakah game dengan difference point yang sangat rendah, cenderung
# menarik perhatian penonton | MERGING DATA TV SHOWS AND SUPERBOWL!
bowls_tvShows = pd.merge(dataShows[dataShows['super_bowl']>=2], dataBowls,
                         on='super_bowl')
print(bowls_tvShows.head())
# using seaborn library to plot
sns.regplot(x='difference_pts', y='share_household', data=bowls_tvShows,
            color='#EB6036', label='Regression Line', scatter=False)
plt.scatter(bowls_tvShows['difference_pts'], bowls_tvShows['share_household'],
            label='Real Data', color='#EE987E')
plt.ylabel('Share Household'); plt.xlabel('Difference Points'); plt.legend()
plt.show()
# CEK RELASI: APAKAH JUMLAH PENONTON AKAN MENINGKATKAN HARGA ADS JUGA?
fig, ax = plt.subplots(3,1)
ax[0].plot(dataShows['super_bowl'], dataShows['avg_us_viewers'], color='#AB845B')
ax[0].set_title('Average Number of US Viewers')
ax[1].plot(dataShows['super_bowl'], dataShows['rating_household'], color='#5E4429')
ax[1].set_title('Household Rating')
ax[2].plot(dataShows['super_bowl'], dataShows['ad_cost'], color='#3D2D5E')
ax[2].set_title('Ad Cost')
plt.ylabel('Super Bowls')
plt.tight_layout()
plt.show()
# MICHAEL JASKON DID PERFORMED ON SUPERBOWLS 27: mari lihat bagaimana kejadian sblm michael jackson!
belowMJ = dataMusicians[dataMusicians['super_bowl']<=27].dropna()
print(belowMJ)
# let's grouping to see which musicians had performed most of the time?
time_appearances = dataMusicians.groupby('musician').count()['super_bowl'].reset_index()
time_appearances = time_appearances.sort_values('super_bowl', ascending=False)
print(time_appearances[time_appearances['super_bowl']>1])
# let's search for musician that has highest number of songs performed
notBands = dataMusicians[~dataMusicians['musician'].str.contains('Marching')]
notBands = notBands[~notBands['musician'].str.contains('Spirit')]
# spirit adalah konvensi penamaan normal untuk marching Band!
maxSongs = int(max(notBands['num_songs'].values))
plt.hist(notBands['num_songs'].dropna(), bins=maxSongs, color='#6CAB75')
plt.ylabel('Number of Songs per Halftime Show Performance')
plt.xlabel('Number of Musicians')
plt.show()
notBands = notBands.sort_values('num_songs', ascending=False)
print(notBands[:10])
