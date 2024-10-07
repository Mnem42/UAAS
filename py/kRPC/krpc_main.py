import krpc
import multiprocessing as mp

def start(ip):
    #try:
        conn = krpc.connect(name="UAAS", address=ip)
        print(conn.krpc.get_status().version)
        make_UI(conn)

   # except ConnectionRefusedError:
    #    print("client does not have a krpc install")
        return conn
        
def make_UI(conn):
    conn = krpc.connect(name='User Interface Example')
    canvas = conn.ui.stock_canvas

    screen_size = canvas.rect_transform.size
    panel = canvas.add_panel()

    rect = panel.rect_transform
    rect.size = (200, 100)
    rect.position = (110-(screen_size[0]/2), 0)


    text = panel.add_text("UAAS")
    text.rect_transform.position = (0, -20)
    text.color = (1, 1, 1)
    text.size = 18
def start_mthread(ip):
    p = mp.Process(target=start, args=(ip,))
    p.start()
    p.join()

    return p;


