import numpy as np

class MultimodalComplexBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with mixed degrees
        polynomial = np.sum(x**4 + 2*x**3 + 3*x**2 + 2*x + 1)
        
        # Trigonometric component with multiple frequencies
        trigonometric = np.sum(np.sin(2*x) + 0.5*np.sin(5*x) + 0.3*np.sin(8*x))
        
        # Radial basis function component with varying widths
        rbf = 0
        for i in range(self.dim):
            rbf += np.exp(-0.5 * np.sum((x - np.sin(i))**2))
            
        # Cross-term interaction with high-frequency modulation
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(3*x[i]) * np.cos(4*x[j]) * np.exp(-0.1*(x[i]-x[j])**2)
                
        # Sine-wave based landscape with varying amplitudes
        wave = 0
        for i in range(self.dim):
            wave += (np.sin(x[i]) + 0.5*np.sin(3*x[i]) + 0.2*np.sin(7*x[i])) * np.exp(-0.05*x[i]**2)
            
        # High-dimensional coupling with chaotic-like behavior
        chaos = 0
        for i in range(self.dim):
            chaos += np.sin(x[i] * np.cos(x[(i+1)%self.dim])) * np.cos(x[i] + x[(i+2)%self.dim])
            
        # Combined landscape with carefully balanced components
        return (0.5 * polynomial + 
                0.3 * trigonometric + 
                0.2 * rbf + 
                0.15 * cross_term + 
                0.25 * wave + 
                0.1 * chaos + 
                0.05 * np.sum(np.sin(x)**6))