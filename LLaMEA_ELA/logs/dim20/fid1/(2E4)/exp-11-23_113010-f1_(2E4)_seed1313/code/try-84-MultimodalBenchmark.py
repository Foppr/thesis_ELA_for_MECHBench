import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic tent map component with varying parameter for complexity
        tent_map = np.sum(0.5 * np.abs(x_norm) + 0.3 * np.abs(x_norm**2) + 0.2 * np.abs(x_norm**3))
        
        # Radial basis function terms with Gaussian peaks at different locations
        rbf_sum = 0.0
        centers = np.linspace(-1, 1, 7)
        for i in range(len(centers)):
            for j in range(self.dim):
                rbf_sum += np.exp(-5 * (x_norm[j] - centers[i%len(centers)])**2)
        
        # Asymmetric polynomial potentials with varying exponents
        asym_poly = np.sum(0.4 * x_norm**11 + 0.3 * x_norm**9 + 0.2 * x_norm**7 + 0.1 * x_norm**5)
        
        # Cross-dimensional coupling with sine-based interaction terms
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling scope
                cross_coupling += np.sin(12 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(8 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Multi-scale harmonic components with varying frequencies
        multi_harmonic = np.sum(np.sin(20 * np.pi * x_norm) + 0.7 * np.sin(35 * np.pi * x_norm) + 0.4 * np.sin(50 * np.pi * x_norm))
        
        # Perturbed saddle point with asymmetric cubic terms
        saddle = np.sum(x_norm**3 * np.cos(10 * np.pi * x_norm) + 0.5 * x_norm**4 * np.sin(7 * np.pi * x_norm))
        
        # Add noise and scale the function
        noise = 0.02 * np.random.random()
        
        return 1.8 * tent_map + 0.9 * rbf_sum + 0.7 * asym_poly + 0.6 * cross_coupling + 0.5 * multi_harmonic + 0.4 * saddle + noise