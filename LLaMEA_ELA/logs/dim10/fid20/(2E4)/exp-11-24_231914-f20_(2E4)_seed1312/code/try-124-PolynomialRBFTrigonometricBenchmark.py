import numpy as np

class PolynomialRBFTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute parameters for radial basis functions and trigonometric components
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (15, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.5, 15)
        self.trig_frequencies = np.random.uniform(1.0, 8.0, dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term with mixed degrees
        base = np.sum(x**2) / self.dim + 0.1 * np.sum(np.abs(x)) / self.dim
        
        # Radial basis function component with varying widths and centers
        rbf_sum = 0.0
        for i in range(len(self.rbf_centers)):
            center = self.rbf_centers[i]
            width = self.rbf_widths[i]
            rbf_sum += np.exp(-np.sum(((x - center) / width)**2) / 2)
        
        # Trigonometric coupling with varying frequencies
        trig_coupling = 0.0
        for i in range(self.dim):
            freq = self.trig_frequencies[i]
            trig_coupling += (np.sin(freq * x[i]) * np.cos(freq * x[i]) + 
                             0.5 * np.sin(2 * freq * x[i]) * np.cos(3 * freq * x[i]) +
                             0.3 * np.sin(4 * freq * x[i]) * np.cos(5 * freq * x[i]))
        
        # Polynomial chaos expansion with mixed terms
        chaos = 0.0
        for i in range(self.dim):
            chaos += (x[i]**3 + 0.5 * x[i]**4 + 0.2 * x[i]**5 + 
                     0.1 * x[i]**6) * np.exp(-0.1 * x[i]**2)
        
        # Multi-scale sine-cosine coupling with amplitude modulation
        multi_scale = 0.0
        for i in range(self.dim - 1):
            multi_scale += (np.sin(x[i]) * np.cos(x[i+1]) * 
                           np.exp(-0.5 * (x[i] - x[i+1])**2) * 
                           (1 + 0.3 * np.sin(2 * x[i])) * 
                           (1 + 0.4 * np.cos(3 * x[i+1])))
        
        # Asymmetric polynomial interaction with exponential decay
        asym_poly = 0.0
        for i in range(self.dim):
            if x[i] >= 0:
                asym_poly += (x[i]**3 + 0.5 * x[i]**4) * np.exp(-0.3 * x[i])
            else:
                asym_poly += (x[i]**3 - 0.5 * x[i]**4) * np.exp(-0.4 * np.abs(x[i]))
        
        # High-frequency oscillatory component with variable amplitude
        high_freq = 0.0
        for i in range(self.dim):
            freq = self.trig_frequencies[i]
            high_freq += (np.sin(15 * freq * x[i]) + 
                         0.8 * np.cos(17 * freq * x[i]) + 
                         0.6 * np.sin(19 * freq * x[i]) + 
                         0.4 * np.cos(21 * freq * x[i])) * np.exp(-0.2 * np.abs(x[i]))
        
        # Multi-modal structure with clustering and varying depths
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += (np.sin(8 * x[i]) + 0.7 * np.cos(9 * x[i]) +
                          0.5 * np.sin(12 * x[i]) + 0.3 * np.cos(14 * x[i]))
        
        # Ruggedness through coupled polynomial terms
        ruggedness = 0.0
        for i in range(self.dim - 2):
            ruggedness += (x[i]**3 * x[i+1]**2 + 
                          x[i+1]**3 * x[i+2]**2) * np.exp(-0.15 * (x[i] - x[i+1])**2)
        
        # Final weighted combination
        return base + 1.8 * rbf_sum + 1.5 * trig_coupling + 1.2 * chaos + \
               1.3 * multi_scale + 1.1 * asym_poly + 1.7 * high_freq + \
               1.0 * multimodal + 0.9 * ruggedness