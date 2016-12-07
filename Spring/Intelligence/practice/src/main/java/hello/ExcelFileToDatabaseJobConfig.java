package hello;

import org.springframework.batch.item.ItemReader;
import org.springframework.batch.item.excel.RowMapper;
import org.springframework.batch.item.excel.mapping.BeanWrapperRowMapper;
import org.springframework.batch.item.excel.poi.PoiItemReader;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.io.ClassPathResource;

/**
 * Created by Andrei on 02-Nov-16.
 */
@Configuration
public class ExcelFileToDatabaseJobConfig {

    @Bean
    ItemReader<Specialization> excelSpecializationReader() {
        PoiItemReader<Specialization> reader = new PoiItemReader<>();
        reader.setLinesToSkip(1);
        reader.setResource((new ClassPathResource("C:\\AplicaAcum.xlsx")));
        reader.setRowMapper(excelRowMapper());
        return reader;
    }

    private RowMapper<Specialization> excelRowMapper() {
        BeanWrapperRowMapper<Specialization> rowMapper = new BeanWrapperRowMapper<>();
        rowMapper.setTargetType(Specialization.class);
        return rowMapper;
    }


}
