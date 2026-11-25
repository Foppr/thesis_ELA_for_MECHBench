import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic logarithmic oscillatory component with multiple frequencies
        log_osc = 0.0
        for i in range(self.dim):
            freq1 = 1.8 + 1.5 * np.log(1.0 + np.abs(x[i]))
            freq2 = 0.9 + 0.7 * np.sin(0.7 * x[i])
            amp1 = 2.2 + 1.3 * np.sin(0.5 * x[i])
            amp2 = 1.4 + 0.9 * np.cos(0.3 * x[i])
            log_osc += amp1 * np.sin(freq1 * x[i] + 0.3 * np.cos(2.0 * x[i])) + \
                      amp2 * np.cos(freq2 * x[i] + 0.4 * np.sin(1.5 * x[i]))
        
        # Dynamic elliptic valley structure with asymmetric parameters
        ellipse_valley = 0.0
        for i in range(self.dim):
            a = 1.7 + 0.9 * np.cos(0.4 * x[i])
            b = 0.9 + 0.7 * np.sin(0.3 * x[i])
            c = 1.4 + 0.5 * np.tan(0.2 * x[i])
            ellipse_valley += ((x[i] - a * np.sin(0.5 * x[i]))**2 / a + 
                              (x[i] - b * np.cos(0.6 * x[i]))**2 / b + 
                              (x[i] - c * np.exp(-0.1 * x[i]))**2 / c)
        
        # Multi-peak trigonometric structure with dynamic phase shifts and Gaussian modulations
        trig_peaks = 0.0
        for i in range(self.dim):
            for j in range(4):
                phase_shift = 0.7 * np.sin(0.8 * x[i] + j)
                amplitude = 1.7 + 1.2 * np.cos(0.5 * x[i])
                gaussian_mod = np.exp(-0.35 * (x[i] - j)**2)
                trig_peaks += amplitude * np.cos(2.7 * x[i] + phase_shift) * gaussian_mod
        
        # Cross-dimensional trigonometric coupling with polynomial interaction
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                poly_interaction = 1.2 + 0.6 * (x[i]**3 + x[j]**3)  # Changed to cubic
                coupling += poly_interaction * np.sin(0.8 * (x[i] + x[j])) * np.cos(0.6 * (x[i] - x[j]))
        
        # Saddle-point with enhanced dynamic modulation and multiple interactions
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 2:
                modulator1 = 0.9 + 0.5 * np.sin(0.6 * x[i]) * np.cos(0.5 * x[i+1])
                modulator2 = 0.7 + 0.4 * np.cos(0.4 * x[i+2]) * np.sin(0.7 * x[i])
                saddle += (x[i]**2 - x[i+1]**2) * modulator1 + (x[i+1]**2 - x[i+2]**2) * modulator2
        
        # High-frequency chaotic component with dynamic amplitude and multiple harmonics
        chaos = 0.0
        for i in range(self.dim):
            amp1 = 0.9 + 0.6 * np.sin(1.5 * x[i])
            amp2 = 0.7 + 0.5 * np.cos(2.0 * x[i])
            chaos += (amp1 * np.sin(11.0 * x[i]) * np.cos(4.5 * x[i]) * 
                     np.exp(-0.18 * x[i]**2) + amp2 * np.cos(9.5 * x[i]) * np.sin(3.8 * x[i]))
        
        # Additional Gaussian peak structure for increased multimodality
        gaussian_peaks = 0.0
        for i in range(self.dim):
            for j in range(5):
                peak_height = 2.5 + 2.0 * np.sin(0.4 * x[i])  # Increased height
                gaussian_peaks += peak_height * np.exp(-0.5 * (x[i] - j)**2)
        
        # Dimensionally adaptive normalization
        dim_factor = 1.3 + 0.4 * np.log(self.dim + 1)
        return (0.19 * log_osc + 0.21 * ellipse_valley + 0.23 * trig_peaks + 
                0.16 * coupling + 0.13 * saddle + 0.09 * chaos + 0.06 * gaussian_peaks) * dim_factor