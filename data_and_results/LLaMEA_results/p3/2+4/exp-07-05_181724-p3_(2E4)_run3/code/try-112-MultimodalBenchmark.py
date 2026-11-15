import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial chaos expansion component with mixed degrees
        poly_chaos = np.sum(0.5 * x_norm**2 + 0.3 * x_norm**3 + 0.2 * x_norm**4 + 0.1 * x_norm**5)
        
        # Radial basis functions with varying widths and centers
        rbf = 0.0
        centers = np.linspace(-0.8, 0.8, 5)
        widths = np.linspace(2.0, 8.0, 5)
        for i, (center, width) in enumerate(zip(centers, widths)):
            rbf += np.exp(-width * (x_norm - center)**2)
        
        # Trigonometric coupling terms with varying frequencies and phases
        trig_coupling = 0.0
        frequencies = [5, 10, 15, 20, 25]
        phases = [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]
        for freq, phase in zip(frequencies, phases):
            trig_coupling += np.sin(freq * x_norm + phase) * np.cos(freq * x_norm + phase)
        
        # Multi-dimensional polynomial interaction with cross-terms
        poly_interaction = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                poly_interaction += (x_norm[i]**2 * x_norm[i+1]**3 + 
                                   0.5 * x_norm[i]**3 * x_norm[i+1]**2 + 
                                   0.3 * x_norm[i]**4 * x_norm[i+1])
        
        # Chaotic sine-cosine polynomial interaction
        chaotic_interaction = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                chaotic_interaction += (np.sin(10 * x_norm[i] * x_norm[i+1]) * 
                                      np.cos(15 * x_norm[i] * x_norm[i+1]) + 
                                      0.4 * np.sin(20 * x_norm[i]**2 * x_norm[i+1]**2) * 
                                      np.cos(25 * x_norm[i]**2 * x_norm[i+1]**2))
        
        # Asymmetric polynomial component
        asym_poly = np.sum(np.abs(x_norm)**3 + 0.5 * np.abs(x_norm)**4)
        
        # Mixed exponential and trigonometric terms
        mixed_exp_trig = np.sum(np.exp(-x_norm**2) * np.sin(8 * x_norm) + 
                               0.3 * np.exp(-2 * x_norm**2) * np.cos(12 * x_norm))
        
        # Higher-order cross-dimensional interactions
        high_order_interaction = 0.0
        if self.dim > 2:
            for i in range(self.dim - 2):
                high_order_interaction += (x_norm[i]**2 * x_norm[i+1]**2 * x_norm[i+2]**3 + 
                                         0.2 * x_norm[i]**3 * x_norm[i+1]**2 * x_norm[i+2])
        
        # Additional noise component
        noise = 0.001 * np.random.random()
        
        # Combine all components with carefully tuned weights
        return (0.25 * poly_chaos + 
                0.2 * rbf + 
                0.15 * trig_coupling + 
                0.12 * poly_interaction + 
                0.1 * chaotic_interaction + 
                0.08 * asym_poly + 
                0.06 * mixed_exp_trig + 
                0.05 * high_order_interaction + 
                noise)