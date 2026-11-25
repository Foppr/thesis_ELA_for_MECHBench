import numpy as np

class FractalTwistBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base fractal grid of Gaussian peaks
        peak_term = 0.0
        grid_size = max(2, int(np.ceil(np.sqrt(self.dim))))
        for i in range(grid_size):
            for j in range(grid_size):
                if i * grid_size + j >= self.dim:
                    break
                peak_x = (i / (grid_size - 1) if grid_size > 1 else 0.5) * 10 - 5
                peak_y = (j / (grid_size - 1) if grid_size > 1 else 0.5) * 10 - 5
                sigma = 0.5 + 0.5 * np.sin(i * j * 0.5)
                peak_term += np.exp(-((x[i] - peak_x)**2 + (x[j] - peak_y)**2) / (2 * sigma**2))
        
        # Sinusoidal twisting field
        twist_term = 0.0
        for i in range(self.dim):
            twist_term += np.sin(x[i] * (1 + 0.1 * np.sin(i * 0.5))) * np.cos(x[i] * (1 + 0.1 * np.cos(i * 0.3)))
        
        # Exponentially decaying correlation between dimensions
        corr_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                corr_term += np.exp(-dist) * (x[i]**2 + x[j]**2)
        
        # Fractal scaling factor based on dimensionality
        scale_factor = 1.0 + 0.2 * np.log(self.dim + 1) + 0.1 * np.sin(self.dim * np.pi / 6)
        
        # Add noise component with chaotic behavior
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(x[i] * (i + 1)) * np.cos(x[i] * (i + 2)) * np.tan(x[i] / (i + 3))
        
        return scale_factor * (0.3 * peak_term + 0.3 * twist_term + 
                              0.2 * corr_term + 0.2 * noise)