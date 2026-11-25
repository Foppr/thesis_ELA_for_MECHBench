import numpy as np

class MultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic sine-wave components with non-linear frequency modulation
        chaotic_sin = np.sum(np.sin(20.0 * np.sin(15.0 * x_scaled)) * 
                           np.cos(18.0 * np.cos(13.0 * x_scaled)) + 
                           0.7 * np.sin(25.0 * np.sin(22.0 * x_scaled**2)) * 
                           np.cos(23.0 * np.cos(19.0 * x_scaled**2)) + 
                           0.4 * np.sin(30.0 * np.sin(27.0 * x_scaled**3)) * 
                           np.cos(28.0 * np.cos(24.0 * x_scaled**3)))
        
        # Adaptive Gaussian peaks with dynamic widths and heights
        adaptive_peaks = np.sum(0.8 * np.exp(-8.0 * (x_scaled - 0.2)**2) + 
                             0.35 * np.exp(-5.0 * (x_scaled + 0.5)**2) + 
                             0.2 * np.exp(-10.0 * (x_scaled - 0.7)**2) + 
                             0.15 * np.exp(-3.0 * (x_scaled + 0.9)**2))
        
        # Cross-dimensional polynomial coupling with exponential interactions
        poly_coupling = np.sum((x_scaled[:-1]**4 + x_scaled[1:]**4) * 
                            np.exp(-2.0 * (x_scaled[:-1] - x_scaled[1:])**2) + 
                            (x_scaled[:-2]**5 + x_scaled[2:]**5) * 
                            np.sin(5.0 * (x_scaled[:-2] + x_scaled[2:])) + 
                            (x_scaled[:-3]**3 + x_scaled[3:]**3) * 
                            np.cos(3.0 * (x_scaled[:-3] - x_scaled[3:])))
        
        # Multi-scale harmonic interference with phase shifts and amplitude modulation
        multi_harmonics = np.sum(np.sin(8.0 * x_scaled) * np.cos(12.0 * x_scaled) * 
                              np.exp(-0.5 * x_scaled**2) + 
                              0.9 * np.sin(14.0 * x_scaled**2) * np.cos(16.0 * x_scaled**2) * 
                              np.exp(-0.3 * x_scaled**2) + 
                              0.6 * np.sin(20.0 * x_scaled**3) * np.cos(22.0 * x_scaled**3) * 
                              np.exp(-0.1 * x_scaled**2))
        
        # Asymmetric landscape with weighted sum of components and conditioning
        condition_factor = np.sum(np.abs(x_scaled)**1.5 + 0.5 * np.sin(10.0 * x_scaled))
        
        return 0.4 * chaotic_sin + 0.3 * adaptive_peaks + 0.15 * poly_coupling + 0.1 * multi_harmonics + 0.05 * condition_factor + 2.1