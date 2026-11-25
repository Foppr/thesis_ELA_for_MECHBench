import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        x = np.clip(x, -5.0, 5.0)
        
        # Asymmetric polynomial potentials with dynamic exponents
        poly_term = 0.0
        for i in range(self.dim):
            if x[i] >= 0:
                exp_val = 3.0 + 0.5 * np.sin(i * 0.8)
                poly_term += (1.5 + 0.3 * np.cos(i * 0.6)) * x[i]**exp_val
            else:
                exp_val = 2.5 + 0.4 * np.cos(i * 0.7)
                poly_term += (1.2 + 0.2 * np.sin(i * 0.5)) * x[i]**exp_val
        poly_term /= self.dim
        
        # Sinusoidal coupling with dynamic frequencies and amplitudes
        sin_coupling = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(i * 0.9) + 0.8 * np.cos(i * 0.6)
            amp = 1.0 + 0.5 * np.cos(i * 0.7) + 0.3 * np.sin(i * 0.4)
            sin_coupling += amp * np.sin(freq * x[i] + 0.5 * np.sin(i * 0.8))
        sin_coupling /= self.dim
        
        # Radial chaotic component with dynamic scaling
        radius = np.sqrt(np.sum(x**2))
        if radius == 0:
            radius = 1e-10
        radial_term = (np.log(radius + 1) * 
                      np.sin(2.5 * radius) * 
                      np.cos(3.5 * radius) * 
                      np.exp(-0.2 * radius) * 
                      (1 + 0.2 * np.sin(0.3 * radius**1.5)))
        
        # Cross-dimensional interaction with chaotic modulation
        cross_term = 0.0
        for i in range(self.dim - 1):
            mod_val = 1.0 + 0.3 * np.sin(i * 0.7) * np.cos((i+1) * 0.5)
            cross_term += mod_val * np.sin(2.0 * (x[i] + x[i+1])) * np.exp(-0.1 * abs(x[i] - x[i+1]))
        cross_term /= (self.dim - 1)
        
        # Multi-scale chaotic modulation with varying periods
        mod_term = 0.0
        for i in range(self.dim):
            period1 = 2.0 + 0.5 * np.sin(i * 0.6)
            period2 = 3.0 + 0.4 * np.cos(i * 0.8)
            mod_term += np.sin(period1 * x[i]) * np.cos(period2 * x[i]) * np.exp(-0.05 * abs(x[i]))
        mod_term /= self.dim
        
        # Asymmetric Gaussian components with dynamic centers and variances
        gaussian_term = 0.0
        for i in range(self.dim):
            center = -4.0 + 8.0 * i / (self.dim - 1) if self.dim > 1 else 0.0
            variance = 0.8 + 0.4 * np.sin(i * 0.7)
            gaussian_term += np.exp(-0.5 * ((x[i] - center) / variance)**2)
        gaussian_term /= self.dim
        
        # Final combination with dynamic weights
        result = (poly_term * 1.8 + 
                 sin_coupling * 1.5 + 
                 radial_term * 0.7 + 
                 cross_term * 1.2 + 
                 mod_term * 0.9 + 
                 gaussian_term * 1.1)
        
        return float(result)