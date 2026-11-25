import numpy as np

class RuggedMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with exponential decay and sinusoidal modulation
        r_squared = np.sum(x_scaled**2)
        radial_term = np.exp(-r_squared / 2.5) * (1.0 + 0.4 * np.sin(6.0 * r_squared))
        
        # Create periodic forcing terms with varying frequencies and amplitudes
        periodic_terms = []
        for i in range(self.dim):
            freq = 1.5 + 4.0 * np.sin(i * np.pi / self.dim)
            amp = 1.2 + 0.3 * np.cos(i * np.pi / 3)
            term = amp * np.sin(freq * x_scaled[i] + i * np.pi/5) * np.cos(freq * x_scaled[i] + i * np.pi/4)
            periodic_terms.append(term)
        
        # Combine periodic terms with cross-correlations
        periodic_sum = np.sum(periodic_terms)
        cross_corr = np.sum(np.sin(2.5 * x_scaled[:-1] + x_scaled[1:]) * np.cos(2.0 * x_scaled[:-1] - x_scaled[1:]))
        
        # Add exponentially decaying correlation structure with modified decay rate
        decay_corr = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_scaled[i] - x_scaled[j])
                decay_corr += np.exp(-dist * 1.5) * np.sin(4.0 * (x_scaled[i] + x_scaled[j]))
        
        # Introduce ruggedness via high-frequency oscillations with modified coefficients
        high_freq = np.sum(np.sin(15.0 * x_scaled) * np.cos(10.0 * x_scaled) + 0.25 * x_scaled**3)
        
        # Combine all terms with conditioning factor
        conditioning_factor = 1.0 + 0.2 * np.sin(2.5 * r_squared)
        
        # Final function value with weighted components
        result = conditioning_factor * (radial_term + 0.6 * periodic_sum + 0.4 * cross_corr + 0.3 * decay_corr + 0.2 * high_freq)
        
        return result