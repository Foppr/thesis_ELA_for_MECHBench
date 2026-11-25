import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Base quadratic term with modified scaling
        quadratic = 0.8 * np.sum(x**2) / self.dim
        
        # Enhanced chaotic multimodal component with increased frequency and amplitude modulation
        periodic = 0.0
        for i in range(self.dim):
            periodic += 3.2 * np.sin(15 * np.pi * x[i]) ** 3 + 1.1 * np.cos(8 * np.pi * x[i]) ** 3
        
        # Modified basin term with additional polynomial interaction
        basin = 0.4 * np.sum((x - 1.8)**2) + 0.05 * np.sum((x - 1.8)**4)
        
        # Intensified noise terms with higher frequency components
        noise = 0.2 * np.sum(np.sin(20 * x) * np.cos(10 * x) * np.sin(5 * x))
        
        # Enhanced saddle point term with higher-order polynomial
        saddle = 0.08 * np.sum(x**6)
        
        # Stronger cross-dimensional interaction terms with non-linear coupling
        cross_interaction = 0.12 * np.sum(np.sin(x[:-1] * x[1:]) * (x[:-1]**2 + x[1:]**2))
        
        # Additional chaotic cross-dimensional coupling term
        chaotic_coupling = 0.03 * np.sum(np.sin(np.pi * np.sum(x**3, axis=0)) * x**2)
        
        return quadratic + periodic + basin + noise + saddle + cross_interaction + chaotic_coupling