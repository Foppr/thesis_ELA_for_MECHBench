import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Highly complex multimodal function with chaotic interactions
        result = (np.sum(x**2) + 
                 2.0 * np.sum(np.sin(25.0 * x)**3) + 
                 1.5 * np.sum(np.exp(-0.3 * x**2)) + 
                 0.8 * np.sum(x**4) + 
                 0.6 * np.sum(np.cos(12.0 * x)**2) + 
                 1.2 * np.sum(np.sin(30.0 * x) * np.cos(15.0 * x)) + 
                 0.5 * np.sum(np.exp(-0.1 * np.abs(x))) + 
                 0.4 * np.sum(np.sin(50.0 * x)**4) + 
                 0.3 * np.sum(x**7) + 
                 0.2 * np.sum(np.exp(-0.05 * x**4)) + 
                 1.0 * np.sum(np.sin(10.0 * x) * np.exp(-0.2 * x**2)) +
                 0.9 * np.sum(np.sin(40.0 * x**2)) +
                 0.7 * np.sum(np.cos(20.0 * x**3)) +
                 1.1 * np.sum(np.exp(-0.15 * x**3)) +
                 0.6 * np.sum(np.tan(8.0 * x)**2) +
                 0.5 * np.sum(np.log(1.0 + np.abs(x))) +
                 0.4 * np.sum(np.sin(60.0 * x) * np.cos(30.0 * x)) +
                 0.3 * np.sum(np.exp(-0.25 * np.abs(x)**2)) +
                 0.2 * np.sum(np.sin(70.0 * x**2) * np.cos(10.0 * x)) +
                 0.1 * np.sum(np.exp(-0.3 * x**6)))
        
        return result