import numpy as np

class ChaoticCoupledMultiModalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for each dimension
        self.center_offsets = np.random.uniform(-2.0, 2.0, dim)
        self.amplitude_factors = np.random.uniform(0.3, 2.5, dim)
        self.frequency_modulators = np.random.uniform(1.2, 2.0, dim)
        self.coupling_strengths = np.random.uniform(0.1, 0.8, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Base quadratic term
        result += 0.15 * np.sum(x**2)
        
        # Multi-modal sinusoidal components with enhanced chaos
        for i in range(self.dim):
            center = 3.0 * np.sin(self.center_offsets[i] * x[i])
            amplitude = self.amplitude_factors[i]
            frequency = 3.0 + self.frequency_modulators[i] * np.sin(1.5 * x[i])
            
            # Enhanced asymmetric sinusoidal contribution
            term = amplitude * (np.sin(frequency * x[i] + center)**3 + 
                               0.7 * np.cos(2.5 * frequency * x[i] + center)**3)
            result += term
            
        # Radial basis functions with chaotic centers
        for i in range(self.dim):
            # Chaotic dynamic center based on position and dimension
            dynamic_center = 2.0 * np.sin(x[i]) + 0.8 * np.cos(3 * x[i]) + 0.3 * np.sin(5 * x[i])
            sigma = 0.4 + 0.4 * np.abs(np.cos(x[i]))
            
            rbf = np.exp(-0.5 * ((x[i] - dynamic_center) / sigma)**2)
            result += 1.0 * rbf
            
        # Enhanced cross-dimensional chaotic coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Chaotic coupling strength with position-dependent modulation
                coupling = (1.5 + 0.4 * np.sin(x[i])) * (1.2 + 0.3 * np.cos(2 * x[j]))
                interaction = coupling * np.sin(1.8 * x[i] + 1.2 * x[j]) * np.cos(0.8 * x[i] - 1.5 * x[j])
                result += 0.4 * interaction
                
        # Enhanced dynamic conditioning based on position
        condition_factor = 1.0 + 0.7 * np.sin(np.sum(x**2) / self.dim + 0.5 * np.cos(np.sum(x)))
        result *= condition_factor
        
        # Add chaotic noise with varying amplitude
        noise_amplitude = 0.08 * (1.0 + 0.3 * np.abs(np.cos(np.sum(x))))
        noise = noise_amplitude * np.sum(np.random.uniform(-1, 1, self.dim))
        result += noise
        
        return result