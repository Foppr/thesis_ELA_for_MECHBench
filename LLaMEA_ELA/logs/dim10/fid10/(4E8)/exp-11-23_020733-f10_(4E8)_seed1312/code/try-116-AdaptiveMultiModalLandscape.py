import numpy as np

class AdaptiveMultiModalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute adaptive parameters for each dimension
        self.center_offsets = np.random.uniform(-1.0, 1.0, dim)
        self.amplitude_factors = np.random.uniform(0.5, 2.0, dim)
        self.frequency_modulators = np.random.uniform(0.8, 1.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Base quadratic term
        result += 0.1 * np.sum(x**2)
        
        # Multi-modal sinusoidal components with adaptive parameters
        for i in range(self.dim):
            center = 2.0 * np.sin(self.center_offsets[i] * x[i])
            amplitude = self.amplitude_factors[i]
            frequency = 2.0 + self.frequency_modulators[i] * np.cos(x[i])
            
            # Asymmetric sinusoidal contribution with modified exponents
            term = amplitude * (np.sin(frequency * x[i] + center)**3 + 
                               0.5 * np.cos(3 * frequency * x[i] + center)**3)
            result += term
            
        # Enhanced radial basis functions with chaotic centers
        for i in range(self.dim):
            # Chaotic dynamic center based on position and dimension
            dynamic_center = 1.5 * np.sin(x[i]) + 0.5 * np.cos(2 * x[i]) + 0.3 * np.sin(3 * x[i])
            sigma = 0.4 + 0.4 * np.abs(np.sin(x[i])) * np.cos(x[i])
            
            rbf = np.exp(-0.5 * ((x[i] - dynamic_center) / sigma)**2)
            result += 1.0 * rbf
            
        # Enhanced cross-dimensional coupling with chaotic interaction
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Chaotic coupling strength with position-dependent modulation
                coupling = (1.0 + 0.4 * np.sin(x[i] + 0.5 * x[j])) * (1.0 + 0.3 * np.cos(2 * x[j]))
                interaction = coupling * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j] + 0.3 * np.sin(x[i]))
                result += 0.4 * interaction
                
        # Enhanced dynamic conditioning based on position
        condition_factor = 1.0 + 0.7 * np.sin(np.sum(x**2) / self.dim + 0.5 * np.cos(np.sum(x)))
        result *= condition_factor
        
        # Add enhanced noise with chaotic amplitude
        noise_amplitude = 0.08 * (1.0 + 0.3 * np.abs(np.sin(np.sum(x)) + 0.2 * np.cos(np.sum(x**2))))
        noise = noise_amplitude * np.sum(np.random.uniform(-1, 1, self.dim))
        result += noise
        
        return result