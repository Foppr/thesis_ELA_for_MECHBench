import numpy as np

class ChaoticCoupledMultiModalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for each dimension
        self.center_offsets = np.random.uniform(-3.0, 3.0, dim)
        self.amplitude_factors = np.random.uniform(0.5, 3.0, dim)
        self.frequency_modulators = np.random.uniform(1.5, 2.5, dim)
        self.coupling_strengths = np.random.uniform(0.2, 1.0, dim)
        self.polynomial_exponents = np.random.uniform(3.0, 6.0, dim)
        self.adaptive_scales = np.random.uniform(0.3, 1.2, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Base quadratic term with adaptive scaling
        adaptive_scale = np.mean(self.adaptive_scales)
        result += 0.2 * adaptive_scale * np.sum(x**2)
        
        # Multi-modal sinusoidal components with nested chaos
        for i in range(self.dim):
            center = 4.0 * np.sin(self.center_offsets[i] * x[i]) + 1.5 * np.cos(2.0 * x[i])
            amplitude = self.amplitude_factors[i]
            frequency = 4.0 + self.frequency_modulators[i] * np.sin(2.0 * x[i] + 0.5 * np.cos(x[i]))
            
            # Nested chaotic sinusoidal contribution with polynomial modulation
            term = amplitude * (np.sin(frequency * x[i] + center)**self.polynomial_exponents[i] + 
                               0.8 * np.cos(3.0 * frequency * x[i] + center)**self.polynomial_exponents[i] +
                               0.5 * np.sin(1.5 * frequency * x[i] + center)**(self.polynomial_exponents[i] + 1))
            result += term
            
        # Enhanced radial basis functions with nested chaotic centers
        for i in range(self.dim):
            # Nested dynamic center based on multiple chaotic functions
            dynamic_center = 3.0 * np.sin(x[i]) + 1.2 * np.cos(3 * x[i]) + 0.8 * np.sin(5 * x[i]) + 0.4 * np.cos(7 * x[i])
            sigma = 0.3 + 0.5 * np.abs(np.cos(x[i] + 0.5 * np.sin(x[i])))
            
            rbf = np.exp(-0.5 * ((x[i] - dynamic_center) / sigma)**2)
            result += 1.5 * rbf
            
        # Enhanced cross-dimensional chaotic coupling with polynomial interaction
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Polynomial coupling strength with position-dependent modulation
                coupling = (2.0 + 0.5 * np.sin(x[i])) * (1.5 + 0.4 * np.cos(2 * x[j])) * (1.0 + 0.3 * np.sin(3 * x[i]))
                interaction = coupling * np.sin(2.0 * x[i] + 1.5 * x[j]) * np.cos(1.0 * x[i] - 1.8 * x[j])
                # Add polynomial interaction term
                interaction += 0.3 * (x[i]**2 + x[j]**2) * np.sin(0.5 * x[i] + 0.7 * x[j])
                result += 0.6 * interaction
                
        # Nested dynamic conditioning based on multiple chaotic functions
        condition_factor = 1.0 + 0.8 * np.sin(np.sum(x**2) / self.dim + 0.6 * np.cos(np.sum(x))) + 0.4 * np.sin(2.0 * np.sum(x))
        result *= condition_factor
        
        # Add nested chaotic noise with varying amplitude and structure
        noise_amplitude = 0.12 * (1.0 + 0.4 * np.abs(np.cos(np.sum(x) + 0.5 * np.sin(np.sum(x)))))
        noise_structure = np.sum(np.random.uniform(-1, 1, self.dim)) + 0.3 * np.sum(np.sin(x))
        result += noise_amplitude * noise_structure
        
        # Add nested polynomial landscape component
        poly_term = 0.05 * np.sum((x**4 + 0.5 * x**3 + 0.2 * x**2)**2)
        result += poly_term
        
        return result