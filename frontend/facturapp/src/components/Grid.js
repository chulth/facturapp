import {View} from 'react-view';
import {styles} from './Styles';
import {Row} from './Rows';

function Grid() {
    const data = [
      [15, 14, 13, 12],
      [11, 10, 9, 8],
      [7, 6, 5, 4],
      [0, 1, 2, 3],
    ];
    return (
      <View style={styles.gridContainer}>
        {data.map((column) => (
          <Row column={column} />
        ))}
      </View>
    );
  }

  export default Grid;