import numpy as np

class ChaoticLogisticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic logistic map parameters
        self.logistic_r = np.random.uniform(3.57, 4.0, dim) * 1.2
        self.logistic_x0 = np.random.uniform(0.1, 0.9, dim) * 0.8
        # Saddle point configuration
        self.saddle_positions = np.random.uniform(-1.0, 1.0, (dim, 3)) * 1.5
        self.saddle_strengths = np.random.uniform(0.5, 2.5, dim) * 1.3
        # Resonance coupling between dimensions
        self.resonance_frequencies = np.random.uniform(0.1, 1.0, (dim, dim)) * 2.0
        self.resonance_amplitudes = np.random.uniform(0.3, 1.5, (dim, dim)) * 1.4
        # Dynamic gradient modulation parameters
        self.gradient_modulators = np.random.uniform(0.8, 2.0, dim) * 1.1
        # Adaptive scaling factors
        self.adaptive_scale = 1.0 + 0.2 * np.random.rand()
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Chaotic logistic map terms
        logistic_term = 0.0
        for i in range(self.dim):
            r = self.logistic_r[i]
            x0 = self.logistic_x0[i]
            # Iterate logistic map for chaotic behavior
            x_val = x0
            for _ in range(10):  # Discard initial transient
                x_val = r * x_val * (1 - x_val)
            # Use final value with sinusoidal modulation
            logistic_val = np.sin(x_val * np.pi) * np.exp(-0.5 * x_norm[i] ** 2)
            logistic_term += logistic_val
            
        # Saddle point terms with adaptive strength
        saddle_term = 0.0
        for i in range(self.dim):
            pos = self.saddle_positions[i]
            strength = self.saddle_strengths[i]
            # Multi-saddle potential function
            saddle_val = 0.0
            for j in range(3):
                saddle_val += strength * (x_norm[i] - pos[j]) ** 2 * np.exp(-0.5 * (x_norm[i] - pos[j]) ** 2)
            saddle_term += saddle_val
            
        # Cross-dimensional resonance coupling
        resonance_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                freq = self.resonance_frequencies[i, j]
                amp = self.resonance_amplitudes[i, j]
                # Resonant interaction with phase coupling
                phase = np.sin(freq * (x_norm[i] + x_norm[j]))
                resonance_val = amp * np.exp(-0.3 * (x_norm[i] ** 2 + x_norm[j] ** 2)) * phase
                resonance_term += resonance_val
                
        # Dynamic gradient modulation
        gradient_term = 0.0
        for i in range(self.dim):
            modulator = self.gradient_modulators[i]
            # Gradient with time-varying modulation
            grad_val = modulator * (x_norm[i] ** 3) * np.cos(2.0 * x_norm[i]) + \
                      0.5 * (x_norm[i] ** 2) * np.sin(x_norm[i])
            gradient_term += grad_val
            
        # Combined terms with adaptive weighting
        result = 1.5 * logistic_term + 1.3 * saddle_term + 1.1 * resonance_term + 1.0 * gradient_term
        
        # Add stochastic noise with chaotic characteristics
        noise_amplitude = 0.02 * (1.0 + 0.03 * self.dim)
        noise = noise_amplitude * np.random.randn()
        
        # Apply adaptive scaling
        result *= self.adaptive_scale
        
        return result + noise