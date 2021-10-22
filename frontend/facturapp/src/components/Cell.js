import {View, Text} from 'react-view'
import {styles} from './Styles'

function Cell({ data }) {
    return (
      <View style={styles.cellStyle}>
        <Text>{data}</Text>
      </View>
    );
  }

export default Cell;