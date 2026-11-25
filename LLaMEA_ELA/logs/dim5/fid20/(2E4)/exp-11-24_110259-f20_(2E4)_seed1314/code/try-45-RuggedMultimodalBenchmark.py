import numpy as np

class RuggedMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with exponential decay and sinusoidal modulation
        r_squared = np.sum(x_scaled**2)
        radial_term = np.exp(-r_squared / 3.0) * (1.0 + 0.3 * np.sin(5.0 * r_squared))
        
        # Create periodic forcing terms with varying frequencies and amplitudes
        periodic_terms = []
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * np.pi / self.dim)
            amp = 1.0 + 0.5 * np.cos(i * np.pi / 4)
            term = amp * np.sin(freq * x_scaled[i] + i * np.pi/6) * np.cos(freq * x_scaled[i] + i * np.pi/3)
            periodic_terms.append(term)
        
        # Combine periodic terms with cross-correlations
        periodic_sum = np.sum(periodic_terms)
        cross_corr = np.sum(np.sin(2.0 * x_scaled[:-1] + x_scaled[1:]) * np.cos(1.5 * x_scaled[:-1] - x_scaled[1:]))
        
        # Add exponentially decaying correlation structure
        decay_corr = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_scaled[i] - x_scaled[j])
                decay_corr += np.exp(-dist) * np.sin(3.0 * (x_scaled[i] + x_scaled[j]))
        
        # Introduce ruggedness via high-frequency oscillations
        high_freq = np.sum(np.sin(12.0 * x_scaled) * np.cos(9.0 * x_scaled) + 0.3 * x_scaled**4)
        
        # Combine all terms with conditioning factor
        conditioning_factor = 1.0 + 0.15 * np.sin(2.0 * r_squared)
        
        # Final function value with weighted components
        result = conditioning_factor * (radial_term + 0.7 * periodic_sum + 0.3 * cross_corr + 0.2 * decay_corr + 0.15 * high_freq)
        
        return result