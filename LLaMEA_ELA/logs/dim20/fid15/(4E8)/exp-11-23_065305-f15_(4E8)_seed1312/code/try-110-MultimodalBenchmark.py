import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Radial polynomial component with asymmetric bell shaping
        radius = np.sqrt(np.sum(x**2))
        radial_poly = (0.5 * radius**4 + 0.3 * radius**3 + 0.1 * radius**2) * np.exp(-radius / 4)
        
        # Chaotic sine-wave modulation with varying frequencies and amplitudes
        sine_modulation = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.5 * i)
            amp = 1.0 + 0.5 * np.cos(0.3 * i)
            sine_modulation += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
        sine_modulation /= self.dim
        
        # Cross-dimensional interaction with exponential coupling and trigonometric mixing
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            cross_interaction += (np.sin(x[i]) * np.cos(x[i+1]) * 
                                np.exp(-0.5 * (x[i] - x[i+1])**2) * 
                                np.sin(1.2 * (x[i] + x[i+1])))
        cross_interaction /= (self.dim - 1)
        
        # Asymmetric multimodal component with multiple local minima peaks
        asymmetric = 0.0
        for i in range(self.dim):
            asymmetric += (np.sin(5 * x[i]) * np.cos(3 * x[i]) + 
                          0.7 * np.sin(8 * x[i]) * np.cos(4 * x[i]) + 
                          0.3 * np.sin(12 * x[i]) * np.cos(6 * x[i]))
        asymmetric /= self.dim
        
        # Polynomial chaos with mixed even and odd powers for complex structure
        poly_chaos = (np.sum(x**11) / (11 * self.dim) + 
                     np.sum(x**9) / (9 * self.dim) + 
                     0.8 * np.sum(x**7) / (7 * self.dim) + 
                     0.6 * np.sum(x**5) / (5 * self.dim) + 
                     0.4 * np.sum(x**3) / (3 * self.dim))
        
        # Unique bell-shaped global minimum configuration
        bell_min = np.exp(-np.sum((x - 1.5)**2) / 2.0)
        
        # Combine all components with carefully tuned weights
        result = (radial_poly * 1.2 + sine_modulation * 1.0 + 
                 cross_interaction * 0.8 + asymmetric * 1.3 + 
                 poly_chaos * 0.9 + bell_min * 0.4)
        
        return float(result)