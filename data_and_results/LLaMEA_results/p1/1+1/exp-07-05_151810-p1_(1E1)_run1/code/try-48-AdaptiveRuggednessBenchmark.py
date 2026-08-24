import numpy as np

class AdaptiveRuggednessBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute correlation matrix for exponential decay
        self.corr_matrix = np.zeros((dim, dim))
        for i in range(dim):
            for j in range(dim):
                self.corr_matrix[i, j] = np.exp(-0.1 * abs(i - j))
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Adaptive ruggedness component with exponential decay
        ruggedness = 0.0
        for i in range(self.dim):
            # Exponentially decaying influence of previous dimensions
            decay_factor = np.exp(-0.2 * i)
            ruggedness += decay_factor * (x[i]**4 - 8*x[i]**2 + 16)
        
        # Multi-modal Gaussian peaks with adaptive amplitudes
        modal_peaks = 0.0
        for i in range(self.dim):
            amplitude = 1.0 + 0.5 * np.sin(0.5 * i)
            peak_center = 3.0 * np.cos(0.3 * i)
            modal_peaks += amplitude * np.exp(-0.5 * ((x[i] - peak_center) / (1.0 + 0.1 * i))**2)
        
        # Correlated noise component
        noise = np.dot(np.dot(x, self.corr_matrix), x)
        
        # Adaptive stiffness region
        stiffness = 1.0 + 0.3 * np.sin(0.7 * np.sum(x**2))
        stiffness_term = stiffness * np.sum(x**2)
        
        # Sine-wave modulation for varying landscape complexity
        modulation = np.sum(np.sin(0.5 * x) * np.cos(0.3 * x))
        
        # Combine all components
        result = ruggedness + modal_peaks + noise + stiffness_term + modulation
        
        return result