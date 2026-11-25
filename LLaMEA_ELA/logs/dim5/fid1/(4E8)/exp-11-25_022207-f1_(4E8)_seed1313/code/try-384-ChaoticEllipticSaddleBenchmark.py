import numpy as np

class ChaoticEllipticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic elliptic parameters with fractal scaling
        self.elliptic_axes = np.logspace(0.3, 4.0, min(25, dim))
        self.saddle_strengths = np.random.uniform(1.0, 5.0, min(20, dim))
        self.conditioning_gradients = np.linspace(0.5, 15.0, min(30, dim))
        # Asymmetric coupling factors with chaotic modulation
        self.asymmetry_factors = np.random.uniform(-0.8, 0.8, min(25, dim))
        # Dynamic modulation frequencies with fractal patterns
        self.modulation_frequencies = np.logspace(0.8, 4.5, min(20, dim))
        # Cross-dimensional coupling with chaotic interaction
        self.cross_coupling_strength = 0.4
        # Noise sensitivity parameters
        self.noise_level = 0.1
        # Fractal interaction coefficients
        self.fractal_coefficients = np.random.uniform(0.2, 1.5, min(30, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Enhanced elliptic contour component with fractal scaling
        elliptic_term = 0.0
        for i in range(min(len(self.elliptic_axes), self.dim)):
            axis = self.elliptic_axes[i]
            fractal = self.fractal_coefficients[i]
            elliptic_term += axis * (x_norm[i] ** 2) * (1.0 + fractal * np.sin(5.0 * x_norm[i]) * np.cos(2.0 * x_norm[i]))
            
        # Chaotic saddle points with superimposed sine-wave patterns
        saddle_term = 0.0
        for i in range(min(len(self.saddle_strengths), self.dim)):
            strength = self.saddle_strengths[i]
            asymmetry = self.asymmetry_factors[i]
            # Add chaotic saddle effect with multiple harmonic components
            saddle_term += strength * (x_norm[i] ** 2) * (
                1.0 + asymmetry * np.sin(3.0 * x_norm[i]) * 
                np.cos(2.0 * x_norm[i]) * 
                np.sin(0.5 * x_norm[i])
            )
            
        # Dynamic conditioning gradients with exponential and hyperbolic scaling
        condition_term = 0.0
        for i in range(min(len(self.conditioning_gradients), self.dim)):
            gradient = self.conditioning_gradients[i]
            # Add hyperbolic and exponential conditioning
            condition_term += gradient * (np.exp(0.3 * np.abs(x_norm[i])) - 1.0) + \
                             0.5 * gradient * np.tanh(2.0 * x_norm[i]) ** 2
            
        # Modulated interaction terms with chaotic cross-dimensional coupling
        modulation_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                freq_i = self.modulation_frequencies[i % len(self.modulation_frequencies)]
                freq_j = self.modulation_frequencies[j % len(self.modulation_frequencies)]
                # Add chaotic cross-dimensional coupling
                coupling = self.cross_coupling_strength * (
                    np.sin(x_norm[i]) * np.cos(x_norm[j]) + 
                    0.3 * np.sin(2.0 * x_norm[i]) * np.cos(0.5 * x_norm[j])
                )
                modulation_term += (
                    np.sin(freq_i * x_norm[i]) * np.cos(freq_j * x_norm[j]) * 
                    (1.0 + coupling) * 
                    np.exp(-0.1 * (x_norm[i] ** 2 + x_norm[j] ** 2))
                )
                
        # Add chaotic noise component
        noise_component = 0.0
        for i in range(self.dim):
            noise_component += self.noise_level * np.sin(10.0 * x_norm[i]) * np.cos(7.0 * x_norm[i])
            
        # Combined landscape with enhanced weighting and chaos
        result = 0.35 * elliptic_term + 0.3 * saddle_term + 0.25 * condition_term + 0.1 * modulation_term + 0.05 * noise_component
        
        return result