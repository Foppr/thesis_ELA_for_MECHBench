import numpy as np

class PolynomialNeuralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Polynomial chaos expansion coefficients
        self.poly_coeffs = np.random.normal(0, 1, size=(dim, 4))
        # Neural network-like adaptive weights
        self.weights = np.random.uniform(-2.0, 2.0, size=(dim, dim))
        # Stochastic resonance parameters
        self.resonance_freq = np.random.uniform(0.1, 2.0, size=dim)
        self.noise_amplitude = np.random.uniform(0.1, 1.0, size=dim)
        # Adaptive scaling factors
        self.adaptive_scale = np.random.uniform(0.5, 2.0, size=dim)
        # Multi-scale harmonic components with enhanced interference
        self.harmonic_freqs = np.random.uniform(1.0, 15.0, size=(dim, 4))
        self.harmonic_amps = np.random.uniform(0.5, 4.0, size=(dim, 4))
        # Additional coupling parameters for better landscape structure
        self.coupling_strength = np.random.uniform(0.5, 2.5, size=dim)
        self.nonlinearity_params = np.random.uniform(0.1, 1.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component with modified weights
        poly_component = 0.0
        for i in range(self.dim):
            x_i = x[i]
            poly_term = (self.poly_coeffs[i, 0] + 
                        self.poly_coeffs[i, 1] * x_i + 
                        self.poly_coeffs[i, 2] * x_i**2 + 
                        self.poly_coeffs[i, 3] * x_i**3)
            poly_component += poly_term * self.adaptive_scale[i]
            
        # Neural network-like adaptive interactions with enhanced coupling
        neural_component = 0.0
        for i in range(self.dim):
            activation = 0.0
            for j in range(self.dim):
                if i != j:
                    activation += self.weights[i, j] * np.tanh(x[j] * self.coupling_strength[j])
            # Enhanced nonlinearity in neural interactions
            neural_component += np.sin(activation * self.nonlinearity_params[i]) * self.adaptive_scale[i]
            
        # Stochastic resonance effect with modified noise characteristics
        resonance_component = 0.0
        for i in range(self.dim):
            # Add more structured noise pattern
            noise = np.random.normal(0, self.noise_amplitude[i], size=2)
            resonance_term = (np.sin(self.resonance_freq[i] * x[i]) + 
                            noise[0] * np.cos(x[i])) * np.exp(-x[i]**2/50.0)
            resonance_component += resonance_term * self.adaptive_scale[i]
            
        # Multi-scale harmonic interference with improved structure
        harmonic_component = 0.0
        for i in range(self.dim):
            harmonic_sum = 0.0
            for k in range(4):
                # Add phase shifts and modified amplitudes for better interference
                phase_shift = np.sin(i * 0.5) if i > 0 else 0
                harmonic_sum += (self.harmonic_amps[i, k] * 
                               np.sin(self.harmonic_freqs[i, k] * x[i] + phase_shift))
            # Add coupling between dimensions for enhanced multimodality
            harmonic_component += harmonic_sum * self.adaptive_scale[i]
            
        # Combined fitness function with optimized importance weights
        return (0.7 * poly_component + 
                1.3 * neural_component + 
                1.0 * resonance_component + 
                1.4 * harmonic_component)