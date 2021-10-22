
import {View} from 'react-view';
import {styles} from './Styles';
import {Cell} from './Cell';

function Row({ column }) {  
  return (
    <View style={styles.rowStyle}>
      {column.map((data) => (
        <Cell data={data} />
      ))}
    </View>
 );
}

export default Row