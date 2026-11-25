import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial terms with varying degrees and adaptive coefficients
        poly_term = np.sum(0.5 * x**6 + 0.3 * x**4 + 0.7 * x**3 + 1.2 * x**2 + 0.8 * x + 0.5)
        
        # Trigonometric components with frequency modulation
        trig_term = np.sum(np.sin(2.0 * x) * np.cos(3.0 * x) + 
                          0.5 * np.sin(5.0 * x) * np.cos(7.0 * x) + 
                          0.3 * np.sin(11.0 * x))
        
        # Radial basis function with dynamic centers and adaptive widths
        rbf_term = 0.0
        centers = np.linspace(-4.0, 4.0, min(20, self.dim))
        for i in range(min(len(centers), self.dim)):
            rbf_term += np.exp(-0.5 * (x[i] - centers[i%len(centers)])**2 / (0.3 + 0.1 * np.sin(i)))
        
        # Cross-dimensional interaction terms
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x[i] * x[j]) * np.sin(0.5 * (x[i] + x[j]))
        
        # Adaptive scaling based on dimensionality
        scale_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        
        # Saddle point enhancement with hyperbolic functions
        saddle_term = np.sum(np.tanh(x)**2 - 0.5 * x**2)
        
        # Noise-like perturbation using discrete cosine transform
        noise_term = 0.0
        for i in range(self.dim):
            noise_term += np.cos((i + 1) * np.pi * x[i] / 5.0) * np.sin((i + 1) * np.pi * x[i] / 5.0)
        
        # Combine all terms with dimensionality-adaptive weights
        return (scale_factor * poly_term + 
                0.7 * trig_term + 
                0.8 * rbf_term + 
                0.6 * cross_term + 
                0.4 * saddle_term + 
                0.3 * noise_term + 
                1.5)