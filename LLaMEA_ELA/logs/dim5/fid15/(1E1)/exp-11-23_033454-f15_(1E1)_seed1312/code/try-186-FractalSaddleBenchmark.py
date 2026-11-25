import numpy as np

class FractalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        # Precompute fractal parameters for each dimension
        self.fractal_freq = 2.0 + 3.0 * np.random.rand(dim)
        self.fractal_amp = 1.0 + 2.0 * np.random.rand(dim)
        self.saddle_pos = 2.5 * np.random.rand(dim) - 1.25
        self.saddle_strength = 0.5 + 2.0 * np.random.rand(dim)
        # Cross-dimension coupling strength
        self.coupling_strength = 0.3 + 0.7 * np.random.rand(dim)
        
    def f(self, x):
        if len(x) != self.dim:
            if len(x) < self.dim:
                x = np.pad(x, (0, self.dim - len(x)), mode='constant', constant_values=0.0)
            else:
                x = x[:self.dim]
        
        # Clip to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal multimodal term
        fractal_term = 0.0
        for i in range(self.dim):
            freq = self.fractal_freq[i] * (1.0 + 0.2 * np.sin(i))
            amp = self.fractal_amp[i] * (1.0 + 0.3 * np.cos(i))
            # Create fractal potential with periodic modulation
            potential = amp * np.sin(freq * x[i])**2 + 0.5 * np.sin(2 * freq * x[i])**2
            fractal_term += potential
        
        # Cross-dimensional coupling term
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = self.coupling_strength[i] * np.cos(x[i] - x[j])**3
                coupling_term += coupling
        
        # Saddle point attraction term
        saddle_term = 0.0
        for i in range(self.dim):
            dist = (x[i] - self.saddle_pos[i])**2
            saddle_term += self.saddle_strength[i] * np.exp(-dist / (2.0 * 0.5**2))
        
        # Add periodic noise component
        noise_term = 0.0
        for i in range(self.dim):
            noise = 0.1 * np.sin(3.0 * x[i] + i) * np.cos(2.0 * x[i] + i)
            noise_term += noise
        
        # Combine all terms with dimensionally varying weights
        total = 0.8 * fractal_term + 0.6 * coupling_term - 0.4 * saddle_term + 0.3 * noise_term
        
        return total