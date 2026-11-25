import numpy as np

class NovelMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for global attraction
        quadratic = np.sum(x_norm ** 2)
        
        # Periodic trigonometric waves with varying frequencies and amplitudes
        wave1 = 2.0 * np.sum(np.sin(8 * x_norm) ** 2 + np.cos(6 * x_norm) ** 2)
        wave2 = 1.5 * np.sum(np.sin(12 * x_norm) * np.cos(10 * x_norm))
        
        # Exponential decay components with position-dependent scaling
        exp_decay1 = 1.2 * np.sum(np.exp(-5 * np.abs(x_norm - 0.3)) * np.sin(4 * x_norm) ** 2)
        exp_decay2 = 0.8 * np.sum(np.exp(-3 * np.abs(x_norm + 0.4)) * np.cos(5 * x_norm) ** 2)
        
        # Asymmetric saddle-point structure with directional bias
        saddle = 1.0 * np.sum((x_norm[:-1] ** 2 - x_norm[1:] ** 2) * np.exp(-0.5 * (x_norm[:-1]**2 + x_norm[1:]**2)))
        
        # Cross-dimensional coupling with asymmetric interaction terms
        cross_coupling = 0.7 * np.sum(np.abs(x_norm[:-1] - x_norm[1:]) * np.sin(3 * x_norm[:-1]) * np.cos(3 * x_norm[1:]))
        
        # Novel logarithmic spiral component with exponential modulation
        spiral = 0.9 * np.sum(np.exp(-0.3 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                             np.sin(5 * np.arctan2(x_norm[1:], x_norm[:-1])) ** 2)
        
        # Asymmetric Gaussian peaks with different widths and positions
        gaussian1 = 1.3 * np.sum(np.exp(-8 * (x_norm - 0.2 * np.sin(3 * x_norm)) ** 2))
        gaussian2 = 0.9 * np.sum(np.exp(-6 * (x_norm + 0.3 * np.cos(4 * x_norm)) ** 2))
        
        # Dimension-dependent conditioning factor
        condition_factor = 1.0 + 0.5 * np.log(self.dim + 1)
        
        # Combine all terms with appropriate scaling
        return condition_factor * (quadratic + wave1 + wave2 + exp_decay1 + exp_decay2 + 
                                 saddle + cross_coupling + spiral + gaussian1 + gaussian2)