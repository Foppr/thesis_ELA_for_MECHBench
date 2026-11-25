import numpy as np

class SelfSimilarSpectralResonanceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        
        # Fractal structure parameters with self-similarity
        self.fractal_base = np.random.uniform(0.5, 2.0, dim)
        self.fractal_exponent = np.random.uniform(0.3, 0.8, dim)
        self.fractal_scale = np.random.uniform(0.1, 1.0, dim)
        
        # Stochastic resonance parameters
        self.resonance_strength = np.random.uniform(0.5, 2.5, dim)
        self.noise_amplitude = np.random.uniform(0.1, 0.8, dim)
        self.resonance_frequency = np.random.uniform(1.0, 5.0, dim)
        
        # Spectral interference parameters
        self.spectral_orders = np.random.randint(3, 8, dim)
        self.spectral_weights = np.random.uniform(0.5, 2.0, (dim, 5))
        self.spectral_phases = np.random.uniform(0, 2*np.pi, (dim, 5))
        
        # Dynamic coupling coefficients
        self.coupling_strength = np.random.uniform(0.1, 1.5, (dim, dim))
        self.coupling_frequency = np.random.uniform(0.5, 3.0, (dim, dim))
        
        # Adaptive scaling factors
        self.adaptive_scale = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Fractal self-similarity structure
        for i in range(self.dim):
            fractal_term = 0.0
            for k in range(10):
                base = self.fractal_base[i]
                exponent = self.fractal_exponent[i]
                scale = self.fractal_scale[i]
                point = base * (k + 1)**exponent
                distance = np.abs(x[i] - point)
                fractal_term += scale * (distance**(-exponent))
            result += fractal_term
            
        # Stochastic resonance effects
        for i in range(self.dim):
            resonance_effect = 0.0
            for k in range(100):
                noise = np.random.normal(0, self.noise_amplitude[i])
                freq = self.resonance_frequency[i]
                resonance_effect += self.resonance_strength[i] * np.sin(freq * x[i] + noise)
            result += 0.5 * np.abs(resonance_effect)
            
        # Spectral wave interference
        for i in range(self.dim):
            spectral_sum = 0.0
            for k in range(5):
                order = self.spectral_orders[i]
                weight = self.spectral_weights[i][k]
                phase = self.spectral_phases[i][k]
                spectral_sum += weight * np.sin(order * x[i] + phase)
            result += 0.3 * np.abs(spectral_sum)**2
            
        # Dynamic dimension coupling
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    strength = self.coupling_strength[i][j]
                    freq = self.coupling_frequency[i][j]
                    coupling_sum += strength * np.sin(freq * (x[i] - x[j]))
            result += 0.4 * coupling_sum**2
            
        # Adaptive scaling
        for i in range(self.dim):
            result += self.adaptive_scale[i] * np.log(1 + np.abs(x[i]))
            
        # Add global nonlinearity and multi-modality
        result += 0.1 * np.sum(np.sin(10 * x)**2)
        
        return result