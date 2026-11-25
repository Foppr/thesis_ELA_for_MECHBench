import numpy as np

class NestedOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Nested quadratic wells with varying depths and centers
        well_terms = np.sum(0.5 * (x_scaled**2 - 0.2)**2 + 
                           0.3 * (x_scaled**2 + 0.4)**2 + 
                           0.2 * (x_scaled**2 - 0.6)**2)
        
        # Trigonometric oscillations with varying frequencies and amplitudes
        trig_terms = np.sum(np.sin(8.0 * x_scaled) * np.cos(6.0 * x_scaled) + 
                           0.7 * np.sin(12.0 * x_scaled**2) * np.cos(10.0 * x_scaled**2) + 
                           0.4 * np.sin(16.0 * x_scaled**3) * np.cos(14.0 * x_scaled**3))
        
        # Asymmetric radial basins with exponential decay
        radial_terms = np.sum(np.exp(-2.0 * (x_scaled**2 + 0.5)**2) * 
                            (1.0 + 0.5 * np.sin(5.0 * x_scaled)))
        
        # Cross-dimensional coupling with polynomial interactions
        cross_terms = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2)**2 * 
                           np.sin(4.0 * (x_scaled[:-1] + x_scaled[1:])) + 
                           (x_scaled[:-2]**3 + x_scaled[2:]**3) * 
                           np.cos(3.0 * (x_scaled[:-2] - x_scaled[2:])))
        
        # Multi-scale harmonic interference with phase shifts
        harmonic_terms = np.sum(np.sin(7.0 * x_scaled) * np.cos(9.0 * x_scaled) + 
                              0.6 * np.sin(11.0 * x_scaled**2) * np.cos(13.0 * x_scaled**2) + 
                              0.3 * np.sin(17.0 * x_scaled**3) * np.cos(19.0 * x_scaled**3))
        
        # Asymmetric landscape with weighted sum of components
        return 0.4 * well_terms + 0.3 * trig_terms + 0.15 * radial_terms + 0.1 * cross_terms + 0.05 * harmonic_terms + 2.1