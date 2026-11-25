import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Chaotic sine-cosine wave interactions with varying frequencies and amplitudes
        wave_term = np.sum(np.sin(7 * x_normalized) * np.cos(6 * x_normalized) + 
                          0.7 * np.sin(11 * x_normalized) * np.cos(3 * x_normalized))
        
        # Asymmetric quartic potentials with different curvature in positive and negative directions
        quartic = np.sum(np.where(x_normalized >= 0, 
                                 0.6 * x_normalized**4 - 0.2 * x_normalized**2,
                                 0.9 * x_normalized**4 - 0.5 * x_normalized**2))
        
        # Non-separable high-order polynomial interactions with cross-dimension dependencies
        poly_interaction = np.sum(x_normalized**5 * np.sin(2 * x_normalized) + 
                                x_normalized**3 * np.cos(4 * x_normalized) + 
                                0.5 * x_normalized**6 * np.sin(x_normalized))
        
        # Enhanced cross-dimensional coupling with adaptive interaction terms
        cross_coupling = 0
        for i in range(self.dim - 1):
            cross_coupling += (x_normalized[i]**2 + x_normalized[i+1]**2) * np.exp(-np.abs(x_normalized[i] - x_normalized[i+1]))
        
        # Add adaptive noise term to increase robustness and challenge optimization algorithms
        noise = 0.1 * np.random.normal(0, 1, self.dim).sum()
        
        # Combine all terms with adjusted weights for balanced contribution
        return wave_term + quartic + poly_interaction + cross_coupling + noise