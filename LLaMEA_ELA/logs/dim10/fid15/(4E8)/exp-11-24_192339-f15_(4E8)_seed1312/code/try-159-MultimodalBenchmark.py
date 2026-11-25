import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Chaotic sine map multimodal component with varying parameters
        chaotic_multimodal = 0
        for i in range(self.dim):
            a = 3.8 + 0.1 * (i % 3)
            b = 0.5 + 0.2 * (i % 4)
            chaotic_multimodal += np.sin(a * x[i]) * np.cos(b * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Radial basis functions with adaptive widths and centers
        rbf = 0
        for i in range(min(5, self.dim)):
            center = -4.0 + 8.0 * (i / max(1, self.dim - 1))
            width = 0.5 + 1.5 * (i / max(1, self.dim - 1))
            rbf += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Quaternion-inspired coupling with exponential modulation
        quaternion = 0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                term1 = np.exp(x[i]**2) * np.sin(x[i+1])
                term2 = np.exp(x[i+1]**2) * np.cos(x[i])
                quaternion += 0.3 * term1 * term2
        
        # Polynomial cross-terms with varying exponents and coefficients
        polynomial = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                exp_i = 3 + (i % 4)
                exp_j = 5 + (j % 3)
                coeff = 0.2 + 0.1 * (i + j) / max(1, self.dim)
                polynomial += coeff * (x[i] ** exp_i) * (x[j] ** exp_j)
        
        # Asymmetric polynomial component
        asymmetric = 0
        for i in range(self.dim):
            asymmetric += 0.25 * x[i]**3 + 0.15 * x[i]**5 + 0.1 * np.abs(x[i])**7
        
        # Dynamic coupling with hyperbolic functions
        hyperbolic_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                hyperbolic_coupling += 0.15 * np.tanh(x[i] + x[j]) * (x[i]**2 + x[j]**2)
        
        # Sine-cosine cross-dimensional interaction
        sincos_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                sincos_interaction += 0.2 * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
        
        # Final combined function with adaptive scaling
        scale_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        return sphere + scale_factor * (0.25 * chaotic_multimodal + 0.2 * rbf + 
                                       0.15 * quaternion + 0.1 * polynomial + 
                                       0.1 * asymmetric + 0.05 * hyperbolic_coupling + 
                                       0.05 * sincos_interaction)