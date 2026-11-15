import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base radial component with exponential decay
        radial = np.sum(np.exp(-0.1 * x**2))
        
        # Trigonometric interference terms with varying frequencies
        trig_interference = np.sum(np.sin(2.0 * np.pi * x) * np.cos(3.0 * np.pi * x))
        
        # Exponential coupling between dimensions with tunable strength
        exp_coupling = 0.5 * np.sum(np.exp(-0.5 * (x[:-1]**2 + x[1:]**2)) * np.sin(x[:-1] * x[1:]))
        
        # Radial symmetry with polynomial modulation
        radial_symmetry = np.sum((1.0 + 0.5 * np.sin(np.pi * np.sqrt(np.sum(x**2)))) * np.exp(-0.2 * np.sum(x**2)))
        
        # Multi-scale oscillatory component
        oscillatory = 0.3 * np.sum(np.sin(5.0 * x) * np.cos(7.0 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Asymmetric exponential perturbations
        asym_exp = 0.4 * np.sum(np.exp(-0.3 * np.abs(x)) * np.sin(0.5 * x)**2)
        
        # Saddle point structure with hyperbolic tangent
        saddle = 0.2 * np.sum(np.tanh(x) * np.cos(x**2))
        
        # Combined result
        result = radial + trig_interference + exp_coupling + radial_symmetry + oscillatory + asym_exp + saddle
        
        return result