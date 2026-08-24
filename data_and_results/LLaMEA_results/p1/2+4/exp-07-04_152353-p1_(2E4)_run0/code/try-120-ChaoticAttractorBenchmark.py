import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Chaotic component with enhanced logistic map-like behavior
        chaotic = 0
        for i in range(self.dim):
            # Increased chaos with parameter modulation
            param = 3.8 + 0.3 * np.sin(i * 0.9)
            chaotic += np.abs(x_normalized[i] * (1 - x_normalized[i]**2) * param)
        
        # Enhanced nested attractor regions with exponential scaling
        attractor = 0
        for i in range(self.dim):
            # Exponential attraction with multi-scale modulation
            scale = 1.0 + 0.5 * np.sin(i * 0.5)
            region = np.abs(x_normalized[i] - np.sin(i * 0.4))**scale + np.abs(x_normalized[i] + np.cos(i * 0.6))**scale
            attractor += region**2.5
            
        # Refined non-smooth component with multi-exponential terms
        smoothness = 0
        for i in range(self.dim):
            # Multi-exponential smoothness with varying exponents
            exp1 = 2.0 + 0.4 * np.sin(i * 0.7)
            exp2 = 1.5 + 0.3 * np.cos(i * 0.8)
            smoothness += (np.abs(x_normalized[i])**exp1 + 0.5 * np.abs(x_normalized[i])**exp2)
            
        # Enhanced discontinuous gradient regions with piecewise functions
        discontinuous = 0
        for i in range(self.dim):
            # Piecewise discontinuity with multiple thresholds
            val = x_normalized[i] * 7
            threshold1 = np.floor(val)
            threshold2 = np.floor(val * 0.5)
            discontinuous += np.abs(val - threshold1) + 0.3 * np.abs(val - threshold2)
            
        # Combine all components with refined weights
        result = 0.3 * f1 + 0.25 * chaotic + 0.2 * attractor + 0.15 * smoothness + 0.1 * discontinuous
        
        # Enhanced perturbation term with multi-frequency sine waves
        perturbation = 0.05 * np.sum(np.sin(x_normalized * 11) * np.cos(x_normalized * 6) * np.sin(x_normalized * 3))
        result += perturbation
        
        return result