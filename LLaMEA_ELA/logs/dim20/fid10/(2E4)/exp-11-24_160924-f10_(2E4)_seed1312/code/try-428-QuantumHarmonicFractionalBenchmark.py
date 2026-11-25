import numpy as np

class QuantumHarmonicFractionalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        
        # Quantum harmonic oscillator parameters
        self.oscillator_freq = np.random.uniform(0.5, 3.0, dim)
        self.oscillator_amp = np.random.uniform(1.0, 5.0, dim)
        self.oscillator_phase = np.random.uniform(0, 2*np.pi, dim)
        
        # Fractional Brownian motion parameters
        self.hurst_exponent = np.random.uniform(0.3, 0.8, dim)
        self.fbm_scale = np.random.uniform(0.5, 2.0, dim)
        
        # Neural network inspired weight modulation
        self.nn_weights = np.random.uniform(-2.0, 2.0, (dim, dim))
        self.nn_bias = np.random.uniform(-1.0, 1.0, dim)
        self.activation_strength = np.random.uniform(0.5, 2.0, dim)
        
        # Adaptive coupling between dimensions
        self.adaptive_coupling = np.random.uniform(-1.0, 1.0, (dim, dim))
        np.fill_diagonal(self.adaptive_coupling, 0.0)
        
        # Multi-frequency sinusoidal components
        self.multi_freq = np.random.uniform(1.0, 10.0, dim)
        self.multi_amp = np.random.uniform(0.5, 3.0, dim)
        
        # Fractal dimension scaling
        self.fractal_dim = np.random.uniform(1.1, 2.9, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Quantum harmonic oscillator components
        for i in range(self.dim):
            oscillator = self.oscillator_amp[i] * np.sin(self.oscillator_freq[i] * x[i] + self.oscillator_phase[i])
            result += oscillator**2
            
        # Fractional Brownian motion approximation
        fbm_sum = 0.0
        for i in range(self.dim):
            # Simple approximation of FBM using multiple sine waves with different frequencies
            fbm_component = 0.0
            for k in range(1, 6):
                freq = k * self.multi_freq[i]
                amp = self.multi_amp[i] / (k ** (self.hurst_exponent[i] + 0.5))
                fbm_component += amp * np.sin(freq * x[i])
            fbm_sum += fbm_component * self.fbm_scale[i]
        result += fbm_sum**2
        
        # Neural network inspired modulation
        for i in range(self.dim):
            neural_input = np.sum(self.nn_weights[i] * x) + self.nn_bias[i]
            activation = np.tanh(self.activation_strength[i] * neural_input)
            result += activation**2
            
        # Adaptive coupling between dimensions
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling = self.adaptive_coupling[i][j] * np.cos(x[i] * x[j])
                    coupling_sum += coupling
        result += coupling_sum
        
        # Multi-frequency sinusoidal components
        multi_sum = 0.0
        for i in range(self.dim):
            freq_component = 0.0
            for k in range(1, 4):
                freq_component += self.multi_amp[i] * np.sin(k * self.multi_freq[i] * x[i])
            multi_sum += freq_component
        result += multi_sum**2
        
        # Fractal dimension scaling
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += (np.abs(x[i]) ** self.fractal_dim[i]) * np.sin(x[i])
        result += fractal_term
        
        # Add small random noise for robustness
        result += np.random.normal(0, 0.1)
        
        return result