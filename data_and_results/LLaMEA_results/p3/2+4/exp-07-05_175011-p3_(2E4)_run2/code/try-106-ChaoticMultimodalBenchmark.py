import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        quadratic = np.sum(x_norm**2)
        
        # Chaotic sine-cosine interaction terms with dynamic frequencies
        chaotic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic frequency based on dimension
                freq_i = 2 * (i + 1)
                freq_j = 2 * (j + 1)
                # Chaotic interaction with sine-cosine products
                chaotic_interaction += np.sin(freq_i * x_norm[i]) * np.cos(freq_j * x_norm[j]) * np.exp(-0.1 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Radial basis function components with varying widths and centers
        rbf = 0.0
        centers = np.linspace(-1, 1, min(5, self.dim))
        for i in range(min(5, self.dim)):
            if i < self.dim:
                # Gaussian RBF with dynamic width
                width = 0.5 + 0.5 * np.sin(i)
                rbf += np.exp(-0.5 * ((x_norm[i] - centers[i])**2) / (width**2))
        
        # Multimodal sinusoidal structure with varying amplitudes and phases
        multimodal = 0.0
        for i in range(self.dim):
            # Increasing frequency and amplitude
            freq = 3 * (i + 1)
            amp = 1.0 + 0.5 * np.sin(i)
            multimodal += amp * np.sin(freq * x_norm[i])**2
        
        # Cross-term with chaotic phase modulation
        cross_term = 0.0
        for i in range(self.dim - 1):
            # Phase modulation with chaotic component
            phase_mod = np.sin(5 * x_norm[i]) * np.cos(3 * x_norm[i+1])
            cross_term += np.sin(x_norm[i] + x_norm[i+1] + phase_mod)**2
        
        # Dynamic global optimum shift with chaotic perturbation
        shift = 0.0
        for i in range(self.dim):
            # Chaotic shift with sinusoidal perturbation
            shift += 0.2 * np.sin(10 * x_norm[i]) * (x_norm[i] - 0.1)**2
        
        # Combine all components with different weights
        return 0.5 * quadratic + 1.5 * chaotic_interaction + 1.0 * rbf + 2.0 * multimodal + 0.8 * cross_term + 0.6 * shift