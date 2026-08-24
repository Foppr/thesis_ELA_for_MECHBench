import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponential decay with multi-scale factors
        exp_decay = np.sum(np.exp(-0.5 * x_norm**2) * np.cos(7 * np.pi * x_norm) * np.sin(3 * np.pi * x_norm))
        
        # Higher-order trigonometric couplings with dynamic frequencies
        trig_coupling = np.sum(np.sin(8 * x_norm) * np.cos(11 * x_norm)) + \
                        0.7 * np.sum(np.sin(15 * x_norm) * np.cos(19 * x_norm)) + \
                        0.3 * np.sum(np.sin(23 * x_norm) * np.cos(27 * x_norm))
        
        # Adaptive conditioning with exponential scaling
        conditioning = np.sum((x_norm**2) * np.exp(-0.2 * np.abs(x_norm)) * np.log(1 + np.abs(x_norm)))
        
        # Non-separable cross-terms with higher-degree polynomials and trigonometric mixing
        cross_poly = np.sum((x_norm[0] * x_norm[1])**7) + \
                     0.5 * np.sum(x_norm**7 * np.sin(4 * np.pi * x_norm) * np.cos(2 * np.pi * x_norm))
        
        # Additional mixed nonlinear coupling terms with hyperbolic functions
        mixed_coupling = 0.4 * np.sum(np.tanh(3 * x_norm) * np.cos(5 * x_norm) * x_norm**4)
        
        # Add a complex noise term with temporal correlation
        noise = 0.02 * np.random.random() + 0.01 * np.sin(10 * np.sum(x_norm))
        
        # Combine all terms to create a multimodal landscape
        return exp_decay + trig_coupling + conditioning + cross_poly + mixed_coupling + noise