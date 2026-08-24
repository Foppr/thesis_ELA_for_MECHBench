import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        result = np.sum(x**2)
        
        # Enhanced periodic sinusoidal components with varying frequencies and amplitudes
        result += 2.0 * np.sum(np.sin(3.0 * np.pi * x) * np.cos(2.0 * np.pi * x))
        
        # Modified asymmetric polynomial distortions with higher-order terms
        poly_distortion = 1.1 * np.sum(x**3 + 0.5 * x**5 + 0.2 * x**7 + 0.08 * x**9)
        
        # Modified interdimensional coupling with logarithmic interaction
        coupling = 0.7 * np.sum(np.log(1.0 + 0.6 * (x[:-1] - x[1:])**2) * np.sin(x[:-1] * x[1:]))
        
        # Additional multimodal peaks using modified Gaussian and cosine combinations
        peaks = 0.7 * np.sum(np.exp(-0.3 * (x**2 - 2.5)**2) * np.cos(5.0 * x)**2)
        
        # Enhanced chaotic perturbation with hyperbolic tangent decay
        chaotic = 0.4 * np.sum(np.tanh(np.exp(-0.5 * x**2)) * np.cos(np.log(np.abs(x) + 1e-6)))
        
        # Additional saddle point perturbations with modified trigonometric functions
        saddle = 0.2 * np.sum(np.sin(0.8 * x) * np.cos(0.5 * x) * np.sin(x**4))
        
        # Novel interaction term combining exponential and polynomial components
        novel_interaction = 0.3 * np.sum(np.exp(-0.15 * np.abs(x)) * x**5)
        
        # Additional complex coupling with cubic interactions
        cubic_coupling = 0.25 * np.sum((x[:-1]**3 - x[1:]**3) * np.sin(x[:-1] + x[1:]))
        
        # High-frequency oscillatory component
        high_freq = 0.18 * np.sum(np.sin(10.0 * x) * np.cos(8.0 * x))
        
        # Slight mutation: altering the coefficient of the polynomial distortion term
        poly_distortion_mutation = 1.2 * np.sum(x**3 + 0.5 * x**5 + 0.2 * x**7 + 0.08 * x**9)
        
        # Slight mutation: altering the chaotic perturbation term
        chaotic_mutation = 0.35 * np.sum(np.tanh(np.exp(-0.5 * x**2)) * np.cos(np.log(np.abs(x) + 1e-6)))
        
        # Slight mutation: altering the saddle point perturbation
        saddle_mutation = 0.22 * np.sum(np.sin(0.8 * x) * np.cos(0.5 * x) * np.sin(x**4))
        
        # Combine all terms
        result = result + poly_distortion_mutation + coupling + peaks + chaotic_mutation + saddle_mutation + novel_interaction + cubic_coupling + high_freq
        
        return result