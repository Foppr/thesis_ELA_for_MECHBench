import numpy as np

class ChaoticHyperbolicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Hyperbolic sine-cosine chaotic component
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sinh(x_scaled[i]) * np.cosh(x_scaled[i]) * np.sin(x_scaled[i]**2)
        
        # Multi-modal peaks with varying amplitudes and positions
        peaks = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(i * 0.3)
            pos = 0.5 * np.cos(i * 0.4)
            peaks += amp * np.exp(-((x_scaled[i] - pos)**2) / (2 * 0.3**2)) * \
                    np.sin(5 * x_scaled[i]) * np.cos(3 * x_scaled[i])
        
        # Saddle point structure with alternating signs
        saddles = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                saddles += (-1)**(i+j) * np.sin(x_scaled[i]) * np.cos(x_scaled[j]) * \
                          np.exp(-((x_scaled[i] - x_scaled[j])**2) / 0.5)
        
        # Cross-dimensional interaction with exponential decay
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_scaled[i] - x_scaled[j])
                interaction += np.exp(-dist) * np.sin(x_scaled[i] * x_scaled[j]) * \
                              np.cos(x_scaled[i]**2 + x_scaled[j]**2)
        
        # Asymmetric hyperbolic component with dimensionally varying parameters
        asymmetric = 0.0
        for i in range(self.dim):
            asym_factor = 1.0 + 0.3 * np.sin(i * 0.5)
            asymmetric += asym_factor * (np.tanh(x_scaled[i]) - np.sinh(x_scaled[i]))**2
        
        # Combined function with carefully balanced weights
        return 0.8 * chaotic + 1.2 * peaks + 0.6 * saddles + 0.4 * interaction + 0.5 * asymmetric