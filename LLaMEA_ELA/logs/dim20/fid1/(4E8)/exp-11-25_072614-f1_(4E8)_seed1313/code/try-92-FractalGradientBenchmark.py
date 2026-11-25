import numpy as np

class FractalGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like terrain using recursive sine-cosine combinations
        fractal_term = 0.0
        for i in range(1, min(6, self.dim + 1)):
            scale = 2 ** i
            fractal_term += np.sum(np.sin(scale * x) * np.cos(scale * x)) / (self.dim * scale)
        
        # Dynamic gradient field with time-varying directional components
        grad_field = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                grad_field += (x[i+1] - x[i])**2 * np.sin(x[i]) * np.cos(x[i+1])
        
        # Spectral interference components with frequency modulation
        spectral_terms = []
        frequencies = np.linspace(1, 10, min(10, self.dim))
        for i, freq in enumerate(frequencies):
            if i < self.dim:
                spectral_terms.append(np.sin(freq * x[i]) * np.cos(freq * x[i]))
        
        # Combine spectral terms with phase coupling
        spectral_sum = np.sum(spectral_terms) if spectral_terms else 0
        phase_coupling = np.prod(np.sin(x)) + np.prod(np.cos(x))
        
        # Multi-scale noise injection with fractal correlation structure
        noise = np.random.normal(0, 0.1, self.dim)
        for i in range(1, self.dim):
            noise[i] += 0.2 * noise[i-1] * np.sin(i * np.pi / self.dim)
        
        # Basin complexity term with polynomial interactions
        basin_complexity = np.sum(x**4) / (self.dim * 10) + np.sum(x**3) / (self.dim * 5)
        
        # Combine all components with dynamic weighting
        total = 0.3 * fractal_term + 0.25 * grad_field + 0.2 * spectral_sum + \
                0.1 * phase_coupling + 0.1 * np.sum(noise**2) / self.dim + 0.05 * basin_complexity
        
        return total