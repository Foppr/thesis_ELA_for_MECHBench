import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.hurst = 0.7 + 0.2 * np.random.random()  # Fractional Brownian motion parameter
        self.fractal_dim = 1.0 + 0.5 * np.random.random()  # Fractal dimension
        self.correlation_matrix = self._generate_correlation_matrix()
        
    def _generate_correlation_matrix(self):
        # Generate correlation matrix with fractal properties
        corr = np.zeros((self.dim, self.dim))
        for i in range(self.dim):
            for j in range(self.dim):
                distance = abs(i - j)
                corr[i, j] = np.exp(-distance ** (2 * self.hurst))
        return corr
    
    def _fractional_brownian_motion(self, x):
        # Generate fractional Brownian motion values
        fbm = np.zeros(self.dim)
        for i in range(self.dim):
            fbm[i] = np.sum(self.correlation_matrix[i, :i] * x[:i])
        return fbm
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize input
        x_norm = x / 5.0
        
        # Base quadratic term
        result = np.sum(x_norm**2)
        
        # Add fractional Brownian motion component
        fbm_values = self._fractional_brownian_motion(x_norm)
        result += 0.5 * np.sum(fbm_values**2)
        
        # Add fractal multimodal component with self-similarity
        fractal_term = 0.0
        for i in range(self.dim):
            # Use multiple scales for fractal behavior
            scale = 2.0 ** (i % 3)
            fractal_term += scale * np.sin(scale * x_norm[i]) * np.cos(scale * x_norm[i] * 0.5)
        result += 0.3 * fractal_term
        
        # Add adaptive correlation structure
        corr_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                corr_term += self.correlation_matrix[i, j] * x_norm[i] * x_norm[j]
        result += 0.2 * corr_term
        
        # Add self-similar harmonic components
        harmonic_term = 0.0
        for i in range(self.dim):
            freq = 2 * np.pi * (i + 1) * (1 + 0.1 * np.sin(i))
            harmonic_term += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i] * 0.7)
        result += 0.15 * harmonic_term
        
        # Add scale-invariant ruggedness with multiple fractal dimensions
        ruggedness = 0.0
        for i in range(self.dim):
            ruggedness += np.sin(10 * x_norm[i]) * np.cos(5 * x_norm[i])
            ruggedness += np.sin(15 * x_norm[i] * 0.5) * np.cos(7 * x_norm[i] * 0.3)
        result += 0.25 * ruggedness
        
        # Add long-range dependence through cumulative effects
        cumulative = 0.0
        for i in range(self.dim):
            cumulative += np.sin(x_norm[i] * (i + 1)) * np.cos(x_norm[i] * (i + 1) * 0.3)
        result += 0.1 * cumulative
        
        # Add global minimum attraction with fractal scaling
        min_attraction = 0.05 * np.sum(x_norm**4)
        result += min_attraction
        
        return result