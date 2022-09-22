
import os
import csv
BASE_DIR=os.path.dirname(os.path.realpath(__file__))

def render_template(v1,v2,v3,v4):
    return f'{{widget type="Magento\CatalogWidget\Block\Product\ProductsList" show_pager="0" products_count="4" template="Magento_CatalogWidget::product/widget/content/grid.phtml" conditions_encoded="^[`1`:^[`type`:`Magento||CatalogWidget||Model||Rule||Condition||Combine`,`aggregator`:`any`,`value`:`1`,`new_child`:``^],`1--1`:^[`type`:`Magento||CatalogWidget||Model||Rule||Condition||Product`,`attribute`:`sku`,`operator`:`()`,`value`:`{v1}, {v2}, {v3}, {v4}`^]^]"}}'
    
def write_dict(dict):
    txt_path=os.path.join(BASE_DIR,'formatted_widget_1.txt')
    try:
        with open(txt_path,'w') as f:
            for k in dict.keys():
                f.write(f'{k} \n {dict[k]} \n\n')
    except:
        print()


def main():
    FILE_PATH=os.path.join(BASE_DIR,'pwe_blogs.csv')

    dict={}
    with open(FILE_PATH) as csv_file:
        csv_reader= csv.reader(csv_file , delimiter=',')
        for row in csv_reader:
            k=row[0]
            vals=[]
            for v in range(1,5):
                val=row[v]
                vals.append(val)
            
            t=render_template(vals[0],vals[1],vals[2],vals[3])
            str=f'{{{t}}}'
            dict.update({k:str})
        write_dict(dict)
        print('WRITTEN')
if __name__=="__main__":
    main()





