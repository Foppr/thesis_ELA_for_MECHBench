import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Multiple Gaussian peaks with varying heights and widths
        peaks = 0
        for i in range(1, 6):
            peak_height = i * 0.5
            peak_width = 0.5 + i * 0.1
            peak_center = np.sin(i * np.pi / 6) * 0.8
            peaks += peak_height * np.exp(-0.5 * ((x_scaled - peak_center) / peak_width)**2)
        
        # Sinusoidal modulation to increase landscape complexity
        sinusoidal = np.sum(np.sin(10 * x_scaled) * np.cos(7 * x_scaled))
        
        # Global spiral basin to attract towards center
        spiral = np.sum((x_scaled**2 + 0.1) * np.exp(-0.1 * np.sum(x_scaled**2)))
        
        # Asymmetric saddle points with cubic terms
        saddle = np.sum(0.5 * x_scaled**3 - 0.3 * x_scaled**5)
        
        # Cross-dimensional coupling with interaction strength increasing with dimension
        coupling = 0
        for i in range(self.dim - 1):
            coupling += (x_scaled[i] * x_scaled[i+1] * 
                       np.sin(5 * (x_scaled[i] + x_scaled[i+1])) * 
                       (i + 1) * 0.1)
        
        # Add a chaotic component using a modified sine map
        chaotic = np.sum(np.sin(15 * x_scaled + np.sin(13 * x_scaled)))
        
        # Combine all components with different weights
        return 2.0 * peaks + 1.5 * sinusoidal + 0.5 * spiral + 0.3 * saddle + 0.2 * coupling + 0.1 * chaotic