import numpy as np

class ChaoticFractalMultiModalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal-like adaptive parameters
        self.fractal_bases = np.random.uniform(0.1, 2.0, dim)
        self.adaptive_centers = np.random.uniform(-3.0, 3.0, dim)
        self.frequency_modulators = np.random.uniform(1.0, 3.0, dim)
        self.asymmetry_params = np.random.uniform(0.5, 1.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Base quadratic term with fractal scaling
        base_term = 0.05 * np.sum(x**2)
        result += base_term
        
        # Fractal-like sinusoidal components with self-similar patterns
        for i in range(self.dim):
            # Fractal base frequency modulation
            fractal_freq = self.fractal_bases[i] * (1.0 + 0.3 * np.sin(x[i] * 0.5))
            # Adaptive center with chaotic component
            adaptive_center = self.adaptive_centers[i] + 0.5 * np.sin(x[i] * 2.0) * np.cos(x[i] * 0.7)
            # Asymmetric interaction
            asym_factor = self.asymmetry_params[i]
            
            term = asym_factor * (np.sin(fractal_freq * x[i] + adaptive_center)**3 + 
                                0.3 * np.cos(2 * fractal_freq * x[i] + adaptive_center)**3)
            result += term
            
        # Adaptive radial basis functions with time-varying centers
        for i in range(self.dim):
            # Time-varying dynamic center based on chaotic modulation
            dynamic_center = 2.0 * np.sin(x[i]) + 0.8 * np.cos(3 * x[i]) + 0.3 * np.sin(5 * x[i])
            # Dynamic sigma with fractal scaling
            sigma = 0.3 + 0.4 * np.abs(np.sin(x[i] * 1.5)) * self.fractal_bases[i]
            
            rbf = np.exp(-0.5 * ((x[i] - dynamic_center) / sigma)**2)
            result += 1.2 * rbf
            
        # Cross-dimensional fractal coupling with chaotic interaction
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Fractal coupling strength with chaotic modulation
                coupling = (1.0 + 0.4 * np.sin(x[i] * 1.2)) * (1.0 + 0.3 * np.cos(x[j] * 1.5))
                # Chaotic interaction term
                chaotic_interaction = coupling * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                result += 0.5 * chaotic_interaction
                
        # Dynamic conditioning with fractal chaos
        condition_factor = 1.0 + 0.8 * np.sin(np.sum(x**2) / self.dim + 0.5 * np.cos(x[0]))
        result *= condition_factor
        
        # Add fractal-like noise with chaotic amplitude modulation
        noise_amplitude = 0.1 * (1.0 + 0.3 * np.abs(np.sin(np.sum(x) * 0.8)))
        noise = noise_amplitude * np.sum(np.random.uniform(-1, 1, self.dim))
        result += noise
        
        # Add fractal harmonic component for additional complexity
        fractal_harmonic = 0.0
        for i in range(self.dim):
            fractal_harmonic += np.sin(x[i] * 7.0) * np.cos(x[i] * 11.0) * np.sin(x[i] * 13.0)
        result += 0.2 * fractal_harmonic
        
        return result