import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Fractal-based parameters with exponential scaling
        self.fractal_exponents = np.logspace(1.0, 3.0, min(12, dim))
        self.harmonic_weights = np.random.uniform(0.1, 2.0, min(15, dim))
        self.phase_modulators = np.linspace(0.5, 3.0, min(10, dim))
        self.asymmetric_factors = np.random.exponential(1.5, min(8, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Initialize result
        result = 0.0
        
        # Fractal harmonic components with exponential coupling
        for i in range(min(len(self.fractal_exponents), self.dim)):
            exp_factor = self.fractal_exponents[i]
            harmonic_term = self.harmonic_weights[i] * np.sin(x_norm[i] ** exp_factor)
            result += harmonic_term
            
        # Dynamic phase modulation with asymmetric influence
        phase_component = 0.0
        for i in range(min(len(self.phase_modulators), self.dim)):
            modulator = self.phase_modulators[i]
            phase_term = np.cos(modulator * x_norm[i] + np.sin(x_norm[i]))
            phase_component += phase_term
            
        # Asymmetric gradient corridors with exponential scaling
        asymmetry_term = 0.0
        for i in range(min(len(self.asymmetric_factors), self.dim)):
            asym_factor = self.asymmetric_factors[i]
            asym_term = asym_factor * np.tanh(x_norm[i] ** 3)
            asymmetry_term += asym_term
            
        # Multi-scale saddle points with chaotic coupling
        saddle_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, min(i + 5, self.dim)):  # Limited interaction range
                coupling_strength = 0.2 * np.sin(i * j / (self.dim + 1))
                saddle = coupling_strength * np.cos(x_norm[i] * x_norm[j])
                saddle_term += saddle
                
        # Fractal coupling with nested harmonic structures
        fractal_nested = 0.0
        for i in range(self.dim):
            if i % 3 == 0:
                fractal_nested += 0.4 * np.sin(x_norm[i] ** 5)
            elif i % 3 == 1:
                fractal_nested += 0.6 * np.cos(x_norm[i] ** 4)
            else:
                fractal_nested += 0.3 * np.tanh(x_norm[i] ** 6)
                
        # Combine all components with dynamic weighting
        result = result + 0.7 * phase_component + 0.4 * asymmetry_term + 0.3 * saddle_term + 0.2 * fractal_nested
        
        # Add chaotic noise with dimensionality-dependent intensity
        noise_amplitude = 0.05 * (1.0 + 0.1 * self.dim)
        noise = noise_amplitude * np.random.standard_cauchy()
        
        return result + noise