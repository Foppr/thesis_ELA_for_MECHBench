import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for dynamic scaling
        self.chaotic_sequence = np.sin(np.arange(1, dim + 1) * np.pi / (dim + 1))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base radial basis function component
        rbfs = 0.0
        for i in range(self.dim):
            rbfs += np.exp(-0.5 * (x[i] - self.chaotic_sequence[i])**2) * np.sin(2.0 * x[i])
        
        # Sinusoidal oscillation with chaotic frequency modulation
        oscillation = 0.0
        for i in range(self.dim):
            freq = 1.0 + 2.0 * np.abs(np.sin(x[i] * self.chaotic_sequence[i]))
            oscillation += np.cos(freq * x[i]) * np.sin(3.0 * x[i])
        
        # Chaotic perturbation term
        chaotic_pert = 0.0
        for i in range(self.dim):
            chaotic_pert += np.sin(x[i] * np.exp(x[i])) * np.cos(x[i] * np.log(np.abs(x[i]) + 1))
        
        # Cross-dimensional interaction with radial scaling
        cross_term = 0.0
        for i in range(self.dim - 1):
            dist = np.sqrt((x[i] - x[i+1])**2 + 0.1)
            cross_term += np.sin(dist) * np.cos(x[i] * x[i+1])
        
        # Polynomial chaos with exponential weighting
        poly_chaos = 0.0
        for i in range(self.dim):
            poly_chaos += (x[i]**3) * np.exp(-0.5 * x[i]**2) * np.sin(4.0 * x[i])
        
        # Multimodal component with multiple peaks
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += np.sin(5.0 * x[i]) * np.cos(7.0 * x[i]) + np.sin(3.0 * x[i])**2
        
        # Sigmoidal scaling with chaotic modulation
        sigmoid_mod = 0.0
        for i in range(self.dim):
            sigmoid_mod += (1.0 / (1.0 + np.exp(-x[i]))) * np.cos(x[i] * self.chaotic_sequence[i])
        
        # Fractal-like interaction with power-law scaling
        fractal_interaction = 0.0
        for i in range(self.dim - 2):
            fractal_interaction += np.sin(x[i] * x[i+1] * x[i+2]) / (np.abs(x[i]) + 1)
        
        # Final combined function with refined weights
        return 0.5 * (rbfs + oscillation + chaotic_pert + cross_term + poly_chaos + multimodal + sigmoid_mod + fractal_interaction)