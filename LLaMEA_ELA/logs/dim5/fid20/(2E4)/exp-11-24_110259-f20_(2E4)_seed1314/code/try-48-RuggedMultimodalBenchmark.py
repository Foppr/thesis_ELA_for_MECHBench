import numpy as np

class RuggedMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with exponential decay and sinusoidal modulation
        r_squared = np.sum(x_scaled**2)
        radial_term = np.exp(-r_squared / 2.5) * (1.0 + 0.35 * np.sin(4.5 * r_squared))
        
        # Create periodic forcing terms with varying frequencies and amplitudes
        periodic_terms = []
        for i in range(self.dim):
            freq = 2.5 + 2.5 * np.sin(i * np.pi / self.dim + 0.5)
            amp = 1.2 + 0.4 * np.cos(i * np.pi / 4 + 0.3)
            term = amp * np.sin(freq * x_scaled[i] + i * np.pi/5) * np.cos(freq * x_scaled[i] + i * np.pi/4)
            periodic_terms.append(term)
        
        # Combine periodic terms with cross-correlations
        periodic_sum = np.sum(periodic_terms)
        cross_corr = np.sum(np.sin(2.5 * x_scaled[:-1] + x_scaled[1:] + 0.2) * np.cos(1.8 * x_scaled[:-1] - x_scaled[1:] + 0.3))
        
        # Add exponentially decaying correlation structure
        decay_corr = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_scaled[i] - x_scaled[j])
                decay_corr += np.exp(-dist * 1.2) * np.sin(3.5 * (x_scaled[i] + x_scaled[j]) + 0.1)
        
        # Introduce ruggedness via high-frequency oscillations
        high_freq = np.sum(np.sin(14.0 * x_scaled) * np.cos(10.0 * x_scaled) + 0.35 * x_scaled**4)
        
        # Combine all terms with conditioning factor
        conditioning_factor = 1.0 + 0.2 * np.sin(2.5 * r_squared)
        
        # Final function value with weighted components
        result = conditioning_factor * (radial_term + 0.75 * periodic_sum + 0.35 * cross_corr + 0.25 * decay_corr + 0.18 * high_freq)
        
        return result