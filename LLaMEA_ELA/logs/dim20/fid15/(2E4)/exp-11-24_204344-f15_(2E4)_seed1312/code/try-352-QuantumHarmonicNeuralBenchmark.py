import numpy as np

class QuantumHarmonicNeuralBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Quantum-inspired harmonic oscillations with phase modulation and superposition
        quantum_term = 0.0
        for i in range(self.dim):
            phase = np.sin(i * 0.8 + self.dim * 0.5) * np.cos(i * 0.6 + self.dim * 0.4)
            freq = 1.0 + 2.0 * np.sin(i * 0.7 + self.dim * 0.3)
            amp = 1.0 + 1.5 * np.cos(i * 0.9 + self.dim * 0.2)
            quantum_term += amp * np.sin(freq * x[i] + phase) * np.cos(freq * x[i] * 0.8 + phase)
        
        # Adaptive neural network-like interactions with dynamic weights and activation
        nn_term = 0.0
        for i in range(self.dim):
            weight = 1.0 + 0.5 * np.sin(i * 0.5 + self.dim * 0.6)
            bias = -2.0 + 4.0 * np.cos(i * 0.4 + self.dim * 0.3)
            activation = 1.0 / (1.0 + np.exp(-weight * x[i] - bias))
            nn_term += activation ** 2
        
        # Spectral decomposition with frequency-based filtering and multi-scale interaction
        spectral_term = 0.0
        for i in range(self.dim):
            freq_band = 0.5 + 3.0 * np.sin(i * 0.6 + self.dim * 0.4)
            filter_response = np.exp(-0.5 * (x[i] * freq_band) ** 2)
            spectral_term += filter_response * np.sin(x[i] * freq_band * 1.5)
        
        # Dynamic coupling with chaotic interaction strength
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Introduce chaotic modulation to coupling strength
                chaos_factor = 1.0 + 0.5 * np.sin(i * j * 0.3 + self.dim * 0.2 + np.sin(x[i] + x[j]))
                strength = chaos_factor * (0.5 + 2.0 * np.sin(i * j * 0.3 + self.dim * 0.2))
                coupling = strength * np.sin(x[i] - x[j]) * np.cos(x[i] + x[j])
                coupling_term += coupling ** 2
        
        # Multi-scale fractal-like structure with self-similar patterns at different resolutions
        fractal_term = 0.0
        for i in range(self.dim):
            scale_factor = 0.3 + 2.5 * np.sin(i * 1.2 + self.dim * 0.5)
            # Add chaotic modulation to scaling factor
            chaos_mod = 1.0 + 0.3 * np.sin(x[i] * 0.7 + self.dim * 0.4)
            fractal_term += scale_factor * chaos_mod * np.sin(x[i] * scale_factor) * np.cos(x[i] * scale_factor * 0.7)
        
        # Adaptive conditioning with dimension-dependent modulation
        cond_term = 0.0
        for i in range(self.dim):
            condition = 1.0 + 0.8 * np.sin(i * 0.9 + self.dim * 0.4)
            cond_term += condition * x[i] ** 4
        
        # Add chaotic modulation to final fitness function
        total = 0.25 * quantum_term + 0.20 * nn_term + 0.18 * spectral_term + 0.15 * coupling_term + 0.12 * fractal_term + 0.07 * cond_term
        
        # Global normalization with chaotic modulation
        global_norm = 1.0 + 0.3 * np.sin(self.dim * 0.7) * np.cos(self.dim * 0.5 + np.sin(x[0] if len(x) > 0 else 0))
        
        return total * global_norm